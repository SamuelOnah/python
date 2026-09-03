from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import Project, Post, Tag, Profile


class Command(BaseCommand):
    help = "Seed the database with placeholder projects and posts you can edit or delete in /admin/."

    def handle(self, *args, **options):
        tag_names = ["Design", "Django", "React", "Writing", "Open source"]
        tags = {name: Tag.objects.get_or_create(name=name, slug=name.lower().replace(" ", "-"))[0] for name in tag_names}

        projects = [
            dict(
                title="Ledger",
                slug="ledger",
                role="Design & development, solo",
                year="2025",
                summary="A simple expense tracker built for small business owners who don't want spreadsheets.",
                body=(
                    "Ledger started from watching people close to me run a business out of a "
                    "notebook and a phone calculator. The goal wasn't more features — it was "
                    "fewer decisions: log a sale, log a cost, see what's left, in three taps.\n"
                    "I designed the brand and interface first, on paper, before writing a line of "
                    "code, then built the backend in Django to keep the whole thing simple to run "
                    "and cheap to host.\n"
                    "It's still early, but it's already the project that taught me the most about "
                    "where design ends and engineering has to take over."
                ),
                link_url="",
                link_label="View live",
                repo_url="https://github.com/",
                status="in_progress",
                featured=True,
                order=1,
                tags=["Django", "Design"],
            ),
            dict(
                title="Studio Mark",
                slug="studio-mark",
                role="Brand & visual identity",
                year="2025",
                summary="A visual identity system — logo, type, and color — built for a small venture I co-founded.",
                body=(
                    "Studio Mark was the identity work behind a venture I helped start: a mark, a "
                    "type pairing, and a color system designed to hold up across a website, a "
                    "product, and printed materials.\n"
                    "I approached it the way I approach most design work — starting from what the "
                    "business actually does and who it's for, rather than starting from a mood "
                    "board. The result had to work as well on a business card as it does on a "
                    "loading screen.\n"
                    "This project is where the designer and the entrepreneur in me overlap most "
                    "directly — building the face of something I also have a stake in."
                ),
                link_url="",
                repo_url="",
                status="live",
                featured=True,
                order=2,
                tags=["Design"],
            ),
            dict(
                title="Coursework Tracker",
                slug="coursework-tracker",
                role="Personal project",
                year="2024",
                summary="A lightweight tool for planning assignments and deadlines across a semester.",
                body=(
                    "Built out of a very ordinary problem: keeping track of what was due, when, "
                    "across too many courses at once. Coursework Tracker is a small Django app "
                    "with a calendar view, priority tags, and reminders.\n"
                    "It's a small project, but it was the first time I built something from a "
                    "database schema through to a styled front end on my own — a first real "
                    "end-to-end build."
                ),
                link_url="",
                repo_url="https://github.com/",
                status="archived",
                featured=True,
                order=3,
                tags=["Django", "Open source"],
            ),
        ]

        for data in projects:
            tag_list = data.pop("tags")
            obj, created = Project.objects.update_or_create(slug=data["slug"], defaults=data)
            obj.tags.set([tags[t] for t in tag_list])
            self.stdout.write(f"{'Created' if created else 'Updated'} project: {obj.title}")

        posts = [
            dict(
                title="Why I design before I code",
                slug="design-before-code",
                dek="Sketching the interface first has saved me more rework than any framework has.",
                body=(
                    "Whenever I skip the design step and go straight to code, I end up rebuilding "
                    "the same screen two or three times. The layout that seemed obvious in my head "
                    "rarely survives contact with real content and real edge cases.\n"
                    "Now every project starts on paper or in a design file, not an editor. I sketch "
                    "the screens, decide what the type and color are actually communicating, and "
                    "only open the terminal once the shape of the thing is settled.\n"
                    "It feels slower at the start. It's faster by the end, because the engineering "
                    "decisions get to follow a plan instead of inventing one as they go."
                ),
                reading_minutes=4,
                tags=["Design", "Writing"],
            ),
            dict(
                title="What building Ledger taught me about scope",
                dek="Notes from turning a notebook-and-calculator habit into actual software.",
                slug="what-ledger-taught-me",
                body=(
                    "Ledger began as a favor — build something simple so a small business could "
                    "stop tracking money in a physical notebook. It stayed simple for exactly as "
                    "long as I resisted adding features nobody asked for.\n"
                    "Every time I added something 'because it would be useful eventually,' the app "
                    "got harder to explain in one sentence, which meant it got harder to actually "
                    "use. Cutting scope turned out to be the real design work, not the interface "
                    "itself.\n"
                    "I'm still building it. But now every new feature has to answer one question "
                    "first: does this make the three-tap version worse?"
                ),
                reading_minutes=4,
                tags=["Django", "Writing"],
            ),
            dict(
                title="The entrepreneur, the engineer, and the designer in the room",
                dek="On wearing three hats without letting any one of them make all the decisions.",
                slug="three-hats-one-room",
                body=(
                    "It's easy to let one identity quietly run the show. The engineer in me wants "
                    "to over-build. The designer wants to keep polishing something no one has used "
                    "yet. The entrepreneur wants to ship before either of them is ready.\n"
                    "What's worked for me is treating each project like it has three stakeholders, "
                    "even when I'm the only person in the room. I ask what the business actually "
                    "needs, what the interface actually communicates, and what the code actually "
                    "has to hold up under — separately, before trying to satisfy all three at "
                    "once.\n"
                    "It's not a clean process. But it's better than letting whichever hat I put on "
                    "first make every call for the rest of the project."
                ),
                reading_minutes=5,
                tags=["Writing"],
            ),
        ]

        now = timezone.now()
        for i, data in enumerate(posts):
            tag_list = data.pop("tags")
            data["published_at"] = now - timezone.timedelta(days=30 * i)
            obj, created = Post.objects.update_or_create(slug=data["slug"], defaults=data)
            obj.tags.set([tags[t] for t in tag_list])
            self.stdout.write(f"{'Created' if created else 'Updated'} post: {obj.title}")

        profile = Profile.load()
        if not profile.bio:
            profile.bio = (
                "I'm an aspiring software engineer, graphic designer, and entrepreneur — three "
                "things that sound like a lot until you notice how often they're really one job. "
                "Most products fail somewhere in the gap between \"it works\" and \"it looks and "
                "feels right,\" and that gap is where I spend most of my time.\n"
                "On the engineering side, I'm building toward solid, practical software — the kind "
                "that's simple to use because the hard decisions were made early, not left for "
                "later. On the design side, I care about visual identity: how a brand's colors, "
                "type, and layout say something before a single word is read. And as an "
                "entrepreneur, I'm drawn to turning both of those into things people actually use.\n"
                "This site is itself an example of that — a Django backend I built and manage, "
                "wrapped in a design I chose deliberately."
            )
            profile.location = profile.location or "Nigeria"
            profile.save()
            self.stdout.write("Seeded profile bio (add a portrait photo from /admin/).")

        self.stdout.write(self.style.SUCCESS("Seed complete. Edit or delete any of this from /admin/."))
