from django.db import models
    from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(_("title"), max_length=255)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    short_description = models.CharField(_("short description"), max_length=255)
    text = models.TextField(_("text"))
    preview_image = models.ImageField(_("preview image"), upload_to="article/previews/%Y/%m")

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")


class ArticleGallery(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name=_("article"), related_name="gallery"
    )
    image = models.ImageField(_("image"), upload_to="article/gallery/%Y/%m")

    class Meta:
        verbose_name = _("Article gallery")
        verbose_name_plural = _("Article galleries")
