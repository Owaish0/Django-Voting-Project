from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# **What `"classes": ["collapse"]` does (short):**

# It **collapses (hides)** that fieldset in the **Django admin UI**.

# **Result:**

# * “Date information” section is **collapsed by default**
# * Admin user can **click to expand** it

# **Used for:**
# Keeping the admin form **clean and less cluttered**.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)