from django.contrib import admin

from memberships.models import Member


# admin.site.register(Member)

admin.site.site_header = "Website"

class MemberAdmin(admin.ModelAdmin):

    # Option to exclude fields from model when is registered in admin
    # exclude = ("unique_code",)

    # Select fields to pt in admin modle Member
    """fields = (
        "name",
        "membership_plan",
        "unique_code",
    )"""

    # Whit a list_display we can select the fields and show the vale

    list_display = ["name","membership_plan","unique_code"]

    list_filter = ["membership_plan"]

    # Change the link when you need access the data detail
    # list_display_links = ["unique_code"]

    search_fields = ("name",)


admin.site.register(Member, MemberAdmin)