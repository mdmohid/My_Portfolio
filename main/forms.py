from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                    "autocomplete": "name",
                    "class": (
                        "w-full rounded-xl border border-slate-700 "
                        "bg-slate-900/80 px-4 py-3.5 text-slate-100 "
                        "placeholder:text-slate-500 outline-none "
                        "transition duration-200 "
                        "focus:border-cyan-400 focus:ring-2 "
                        "focus:ring-cyan-400/20"
                    ),
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                    "class": (
                        "w-full rounded-xl border border-slate-700 "
                        "bg-slate-900/80 px-4 py-3.5 text-slate-100 "
                        "placeholder:text-slate-500 outline-none "
                        "transition duration-200 "
                        "focus:border-cyan-400 focus:ring-2 "
                        "focus:ring-cyan-400/20"
                    ),
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "placeholder": "What would you like to discuss?",
                    "class": (
                        "w-full rounded-xl border border-slate-700 "
                        "bg-slate-900/80 px-4 py-3.5 text-slate-100 "
                        "placeholder:text-slate-500 outline-none "
                        "transition duration-200 "
                        "focus:border-cyan-400 focus:ring-2 "
                        "focus:ring-cyan-400/20"
                    ),
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Write your message here...",
                    "rows": 6,
                    "class": (
                        "w-full resize-none rounded-xl border border-slate-700 "
                        "bg-slate-900/80 px-4 py-3.5 text-slate-100 "
                        "placeholder:text-slate-500 outline-none "
                        "transition duration-200 "
                        "focus:border-cyan-400 focus:ring-2 "
                        "focus:ring-cyan-400/20"
                    ),
                }
            ),
        }

    def clean_message(self):
        message = self.cleaned_data["message"]

        if len(message.strip()) < 10:
            raise forms.ValidationError(
                "Please enter a message of at least 10 characters."
            )

        return message