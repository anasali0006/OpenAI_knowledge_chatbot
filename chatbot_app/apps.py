from django.apps import AppConfig



class ChatbotAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chatbot_app"

    def ready(self):

        # will initialize the default documents and redis here so redis is up with required docs before application starts

        chunks_for_chatbot = [
            {'text':"HIV/AIDS: There were an estimated 1.5 million new human\
            immunodeficiency virus (HIV) infections globally in 2021, almost one third\
            fewer than in 2010. Effective HIV treatment has also cut global AIDSrelated\
            deaths by 52 per cent, from 1.4 million in 2010 to 650,000 in 2021.\
            Sub-Saharan Africa, the region with the largest HIV burden, has achieved\
            a 44 per cent decline in annual new HIV infections since 2010. However,\
            the decline has been much sharper among males than among females.\
            Fewer children were accessing treatment than adults. The aforementioned\
            inequalities and others faced by key populations at increased risk of HIV are\
            slowing progress towards ending AIDS. Moreover, new infections are rising\
            in some regions, and the world is off track to meet the targets of fewer than\
            370,000 new HIV infections by 2025."},

            {'text':"Tuberculosis (TB): The COVID-19 pandemic has severely impacted access\
            to tuberculosis diagnosis and treatment in many countries, resulting in an\
            increase in the TB disease burden globally. In 2021, an estimated 10.6 million\
            people fell ill with TB, an increase from 10.1 million in 2020. The TB incidence\
            rate also rose by 3.6 per cent between 2020 and 2021, reversing the decline\
            of 2 per cent per year observed for most of the previous two decades. There\
            were an estimated 1.6 million deaths from TB in 2021, an increase of 14.1 per\
            cent from 2020. This is the first time in nearly two decades that the number\
            of TB deaths has increased. Between 2015 and 2021, the net reductions in\
            TB incidence and death were 10 per cent and 5.9 per cent, respectively, only\
            one-fifth and one-tenth of the way to the 2025 milestone of WHO’s End TB\
            Strategy."},

            {'text': "Tuberculosis (TB): The COVID-19 pandemic has severely impacted access\
            to tuberculosis diagnosis and treatment in many countries, resulting in an\
            increase in the TB disease burden globally. In 2021, an estimated 10.6 million\
            people fell ill with TB, an increase from 10.1 million in 2020. The TB incidence\
            rate also rose by 3.6 per cent between 2020 and 2021, reversing the decline\
            of 2 per cent per year observed for most of the previous two decades. There\
            were an estimated 1.6 million deaths from TB in 2021, an increase of 14.1 per\
            cent from 2020. This is the first time in nearly two decades that the number\
            of TB deaths has increased. Between 2015 and 2021, the net reductions in\
            TB incidence and death were 10 per cent and 5.9 per cent, respectively, only\
            one-fifth and one-tenth of the way to the 2025 milestone of WHO’s End TB\
            Strategy."}
        ]






        pass
