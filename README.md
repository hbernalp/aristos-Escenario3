Con Base ne la solicitud, realizaremos un proyecto utilizando el proyecto test-gcp usado en el escenario2, para esto utilizamos el servicio de Google Cloud Build

El flujo a utilizar para ejecutar las actividades son los siguientes:

    - Preparar proyecto (APIs + Artifact Registry).
    - Crear la app simple (Flask), Dockerfile y cloudbuild.yaml.
    - Crear repo en GitHub y subir código.
    - Conceder permisos a la cuenta de Cloud Build.
    - Crear trigger en Cloud Build (conectar GitHub).
    - Hacer push a main → Cloud Build construye, sube la imagen y despliega a Cloud Run.
    - Verificar la URL del servicio y hacer pública la app.
    - Recolectar evidencias de manera transversal, mientras ejecuto la actividad.

Para el desarrollo del proyecto aprovecharemos las variables que ya tenemos

    Project ID: test-gcp-473921
    Project number: 768653268457
    Region: us-central1
    Cloud Run service name (ejemplo): cloudrun-web-app
    Artifact Registry repo (ejemplo): web-repo

1. Preparar proyecto

    1.1. Autenticar y configurar el proyecto

        Para esto utilizaremos los siguientes comandos:

            - gcloud auth login
            - gcloud config set project test-gcp-473921
            - gcloud config set run/region us-central1

![Proyecto, Region y Zona](img/autenticar.png)

    1.2. Habilitar las APIS necesarias, para los artefactos, el cloudbuil y el run, para esto se utiliza el siguiente comando:

        gcloud services enable cloudbuild.googleapis.com run.googleapis.com artifactregistry.googleapis.com

![Proyecto, Region y Zona](img/Apis.png)

    1.3. Creando el repositorio Docker en Artifact Registry
        Para ello se hace uso del siguiente comando:
            gcloud artifacts repositories create web-repo --repository-format=docker --location=us-central1 --description="Repo Docker para Cloud Build / Cloud Run"

![Proyecto, Region y Zona](img/dockerArtifact.png)

        se verifica que haya quedado creado el repositorio

            gcloud artifacts repositories list --location=us-central1

![Proyecto, Region y Zona](img/Registry_Artefact.png)

2. Creando la aplicación simple localmente