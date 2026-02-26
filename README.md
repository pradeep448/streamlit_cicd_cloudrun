gcloud builds submit --tag gcr.io/project-bbfa6ceb-973a-4bb1-a2d/streamlit --project=project-bbfa6ceb-973a-4bb1-a2d

gcloud run deploy --image gcr.io/project-bbfa6ceb-973a-4bb1-a2d/streamlit --platform managed --project=project-bbfa6ceb-973a-4bb1-a2d --allow-unauthenticated