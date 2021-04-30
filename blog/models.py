from django.db import models
from django.contrib.auth.models import User

categories = [
    ("accomodation", "Accomodation"),
    ("advice", "Advice"),
    ("books",  "Books and Novels"),
    ("beauty", "Beauty"),
    ("business", "Business"),
    ("computer-science", "Computer Science"),
    ("cooking", "Cooking"),
    ("comedy", "Comedy"),
    ("corruption", "Corruption"),
    ("crime", "Crime"),
    ("counselling", "Counselling"),
    ("challenge", "Challenge"),
    ("crypto", "Crypto"),
    ("drama", "Drama"),
    ("economy", "Economy"),
    ("education", "Education"),
    ("entertainment", "Entertainment"),
    ("engineering", "Engineering"),
    ("employment", "Employment"),
    ("fitness", "Fitness"),
    ("fashion", " Fashion and Beauty"),
    ("food",  "Foods and Nutrition"),
    ("fashion", "Fashion"),
    ("fuel_subsidy", "Fuel Subsidy"),
    ("food", "Foods"),
    ("forsale", "For Sale"),
    ("graphics", "Grpahics design"),
    ("gossip",  "Gossip"),
    ("giveaway",  "Giveaway"),
    ("hair-style", "Hair style"),
    ("health", "Health"),
    ("insecurity", "Insecurity"),
    ("jokes", "Jokes"),
    ("love", "Love"),
    ("marriage", "Marriage"),
    ("maintenance", "Maintenance"),
    ("movie", "Movie"),
    ("media", "Media"),
    ("music", "Music"),
    ("nutrition", "Nutrition"),
    ("telecom", "Telecom"),
    ("medical", "Medical"),
    ("psychology", "Psychology"),
    ("politics",  "Politics"),
    ("Quotes", "Quotes"),
    ("Relationship", "Relationship"),
    ("religion", "Religion"),
    ("riddles", "Riddles"),
    ("sex-education", "Sex Education"),
    ("sports", "Sports"),
    ("strike", "Strike"),
    ("scarcity", "Scarcity"),
    ("security", "Security"),
    ("skin-care", "Skin Care"),
    ("story", "Story"),
    ("tricks_and_hacks",  "Tricks and Hacks"),
    ("technology", "Technology"),
    ("transport", "Transport"),
    ("violence", "Violence"),
    ("wealth", "Wealth"),
    ("others", "Others")
]


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    category = models.CharField(
        max_length=100, choices=categories, default='Others')
    link_title = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='article_images')
    content = models.TextField()
    must_read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        new_link = self.title.replace(' ', '-') + f'{self.id}'
        self.link_title = new_link

        # formatting html texts output
        self.content = self.content.replace('##h', '</h4>')
        self.content = self.content.replace('#h', '<h4>')
        self.content = self.content.replace('##i', '</i>')
        self.content = self.content.replace('#i', '<i>')
        self.content = self.content.replace('##b', '</b>')
        self.content = self.content.replace('#b', '<b>')
        self.content = self.content.replace('##bq', '</blockquote>')
        self.content = self.content.replace('#bq', '<blockquote>')

        super().save(args, kwargs)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Articles'

# #b## goes here #b## #:< ##:>
# comment model


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.comment}'

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Comments'
