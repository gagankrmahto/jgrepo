from django.db import models

# Create your models here.
class LegalDoc(models.Model):
    doc_id = models.AutoField(primary_key=True)
    document_title = models.CharField(("Breifly mention the title for the doc: "), max_length=100)
    document_doc_url = models.FileField(("Upload the supporting document"),upload_to='legal_docs')
    upload_date = models.DateField(("Date of upload "), auto_now=True)
    def __str__(self):
        return f"{self.document_title}"