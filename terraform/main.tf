provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

resource "google_storage_bucket" "backup_bucket" {
  name          = "my-backup-bucket"
  location      = "US"
  versioning {
    enabled = true
  }
}
