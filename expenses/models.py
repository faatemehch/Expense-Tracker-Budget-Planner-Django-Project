from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    CATEGORY_ICONS = (
        ("utensils", _("Food")),
        ("car", _("Transportation")),
        ("home", _("Housing")),
        ("shopping-cart", _("Shopping")),
        ("film", _("Entertainment")),
        ("heart", _("Health")),
        ("lightbulb", _("Utilities")),
        ("book", _("Education")),
    )
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("user"))
    icon = models.CharField(max_length=30, blank=True, default='receipt', choices=CATEGORY_ICONS,
                            verbose_name=_("Icon"))  # Font-Awesome class

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.name)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 verbose_name=_("Amount"),
                                 validators=[
                                     MinValueValidator(
                                         0.01,
                                         message=_("Expenses must be at least $0.01.")),
                                     MaxValueValidator(
                                         100000,
                                         message=_("Expenses must be at most $10000."))
                                 ])
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category,
                                 related_name="expenses",
                                 verbose_name=_("Category"),
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name=_("Description"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return f"{self.amount} - {self.category} - {self.date}"


class Budget(models.Model):
    PERIOD_CHOICES = [
        ('D', _('Daily')),
        ('W', _('Weekly')),
        ('M', _('Monthly')),
        ('Y', _('Yearly')),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=1, choices=PERIOD_CHOICES, default='M')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Budget: {self.amount} for {self.category}"

