from django.db import models


class SecFiling(models.Model):
    cik = models.CharField(
        max_length=10, db_index=True
    )  # Central Index Key, 10 digit number provided by the SEC
    ticker = models.CharField(max_length=10, db_index=True)
    form_type = models.CharField(max_length=50)  # 10-K, 10-Q, 8-K...
    period_end = models.DateField()
    local_path = models.CharField(max_length=500)
    format = models.CharField(max_length=20)  # ixbrl | xbrl | html
    parsed_at = models.DateTimeField(null=True, blank=True)
    parse_ok = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ticker} {self.form_type}"


class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=10, unique=True)
    isin = models.CharField(
        max_length=20, unique=True, blank=True, null=True
    )  # International Securities Identification Number
    figi = models.CharField(
        max_length=20, unique=True, blank=True, null=True
    )  # Financial Instrument Global Identifier
    country = models.CharField(max_length=50, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    listing_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.ticker})"


class Earnings(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    period = models.CharField(max_length=100)
    report_date = models.DateField()
    eps_basic = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True
    )
    eps_diluted = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True
    )
    net_income = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"{self.company.ticker} - {self.period}"
