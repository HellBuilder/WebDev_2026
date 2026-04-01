from django.core.management.base import BaseCommand

from api.models import Category, Product


class Command(BaseCommand):
    help = "Seed exactly 4 categories and 20 products (5 each)."

    def handle(self, *args, **options):
        catalog = [
            {
                "name": "Smartphones",
                "products": [
                    {
                        "name": "Apple iPhone 15 128GB",
                        "price": 439990,
                        "description": (
                            "A modern iPhone with a bright OLED display and strong everyday performance. "
                            "The camera system captures crisp photos in daylight and low light. "
                            "It is a reliable choice for users who want long software support."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1696446701905-8b34f2f33e0b",
                        "product_url": "https://kaspi.kz/shop/p/apple-iphone-15-128gb-113252342/",
                        "count": 18,
                        "is_active": True,
                    },
                    {
                        "name": "Samsung Galaxy A55 5G 256GB",
                        "price": 224990,
                        "description": (
                            "This mid-range Samsung phone offers a smooth 120Hz display and balanced battery life. "
                            "Its cameras produce natural colors for social media and daily shots. "
                            "The device is ideal for users who need stable performance at a fair price."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf",
                        "product_url": "https://kaspi.kz/shop/p/samsung-galaxy-a55-5g-256gb-117420102/",
                        "count": 25,
                        "is_active": True,
                    },
                    {
                        "name": "Xiaomi Redmi Note 13 Pro 256GB",
                        "price": 169990,
                        "description": (
                            "Redmi Note 13 Pro delivers high value with a sharp display and fast charging. "
                            "The phone handles browsing, maps, and streaming without noticeable lag. "
                            "It fits students and professionals looking for practical features."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97",
                        "product_url": "https://kaspi.kz/shop/p/xiaomi-redmi-note-13-pro-256gb-117498344/",
                        "count": 31,
                        "is_active": True,
                    },
                    {
                        "name": "Google Pixel 8 128GB",
                        "price": 329990,
                        "description": (
                            "Google Pixel 8 focuses on clean Android and excellent computational photography. "
                            "Photos are detailed, and the interface feels fast with minimal preinstalled apps. "
                            "It is a strong option for users who prefer a simple software experience."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab",
                        "product_url": "https://kaspi.kz/shop/p/google-pixel-8-128gb-114640732/",
                        "count": 12,
                        "is_active": True,
                    },
                    {
                        "name": "HONOR X9b 256GB",
                        "price": 154990,
                        "description": (
                            "HONOR X9b comes with a large curved screen and impressive battery endurance. "
                            "It is comfortable for long reading sessions, videos, and messaging. "
                            "The phone is well suited for users who prioritize design and runtime."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1605236453806-6ff36851218e",
                        "product_url": "https://kaspi.kz/shop/p/honor-x9b-256gb-117104201/",
                        "count": 27,
                        "is_active": True,
                    },
                ],
            },
            {
                "name": "Laptops",
                "products": [
                    {
                        "name": "Apple MacBook Air 13 M2 16GB/512GB",
                        "price": 799990,
                        "description": (
                            "MacBook Air with M2 is light, quiet, and highly efficient for daily work. "
                            "It handles coding, document editing, and multitasking with stable performance. "
                            "Battery life is strong enough for a full workday away from a charger."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8",
                        "product_url": "https://kaspi.kz/shop/p/apple-macbook-air-13-m2-16gb-512gb-112484992/",
                        "count": 9,
                        "is_active": True,
                    },
                    {
                        "name": "ASUS Vivobook 15 i5/16GB/512GB SSD",
                        "price": 319990,
                        "description": (
                            "ASUS Vivobook 15 is a practical laptop for office tasks and online meetings. "
                            "The processor and memory combination keeps the system responsive in everyday use. "
                            "It is a balanced choice for students and remote employees."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853",
                        "product_url": "https://kaspi.kz/shop/p/asus-vivobook-15-i5-16gb-512gb-ssd-119842675/",
                        "count": 14,
                        "is_active": True,
                    },
                    {
                        "name": "Lenovo IdeaPad Slim 3 Ryzen 5/8GB/512GB",
                        "price": 274990,
                        "description": (
                            "IdeaPad Slim 3 offers reliable speed for browser-heavy workflows and study platforms. "
                            "The keyboard is comfortable for long typing sessions and note-taking. "
                            "It provides good value for users who need a daily productivity machine."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed",
                        "product_url": "https://kaspi.kz/shop/p/lenovo-ideapad-slim-3-ryzen-5-8gb-512gb-118274104/",
                        "count": 20,
                        "is_active": True,
                    },
                    {
                        "name": "HP Pavilion 14 i7/16GB/1TB SSD",
                        "price": 469990,
                        "description": (
                            "HP Pavilion 14 combines a compact body with enough power for advanced office workloads. "
                            "Fast storage keeps apps and large files opening quickly throughout the day. "
                            "It is suitable for analysts, managers, and frequent travelers."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2",
                        "product_url": "https://kaspi.kz/shop/p/hp-pavilion-14-i7-16gb-1tb-ssd-118501230/",
                        "count": 11,
                        "is_active": True,
                    },
                    {
                        "name": "Acer Nitro V 15 i5/16GB/512GB RTX 4050",
                        "price": 529990,
                        "description": (
                            "Acer Nitro V 15 is designed for gaming and GPU-heavy software tasks. "
                            "It delivers smooth frame rates in popular titles at Full HD settings. "
                            "The cooling system keeps performance consistent during long sessions."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6",
                        "product_url": "https://kaspi.kz/shop/p/acer-nitro-v-15-i5-16gb-512gb-rtx-4050-119114907/",
                        "count": 7,
                        "is_active": True,
                    },
                ],
            },
            {
                "name": "Home Appliances",
                "products": [
                    {
                        "name": "LG F2V5HS0W Washing Machine 7kg",
                        "price": 214990,
                        "description": (
                            "This LG washing machine supports multiple fabric programs and stable spin performance. "
                            "The drum is gentle on clothes while still removing everyday dirt effectively. "
                            "It is a dependable option for apartments and small families."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1",
                        "product_url": "https://kaspi.kz/shop/p/lg-f2v5hs0w-7kg-100456781/",
                        "count": 13,
                        "is_active": True,
                    },
                    {
                        "name": "Samsung RT38K5532S8 Refrigerator",
                        "price": 359990,
                        "description": (
                            "Samsung RT38 refrigerator keeps temperature stable and compartments well organized. "
                            "The shelf layout makes it easy to store fresh produce and large containers. "
                            "It works well for families that cook often at home."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5",
                        "product_url": "https://kaspi.kz/shop/p/samsung-rt38k5532s8-101992345/",
                        "count": 6,
                        "is_active": True,
                    },
                    {
                        "name": "Xiaomi Mi Smart Air Fryer 3.5L",
                        "price": 48990,
                        "description": (
                            "Mi Smart Air Fryer prepares crispy meals using less oil than traditional frying. "
                            "Preset modes simplify cooking for chicken, vegetables, and frozen snacks. "
                            "It is compact enough for kitchens with limited counter space."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c",
                        "product_url": "https://kaspi.kz/shop/p/xiaomi-mi-smart-air-fryer-3-5l-104998562/",
                        "count": 29,
                        "is_active": True,
                    },
                    {
                        "name": "Philips GC4537/70 Steam Iron",
                        "price": 32990,
                        "description": (
                            "This Philips steam iron heats quickly and maintains consistent steam output. "
                            "The soleplate glides smoothly over cotton and synthetic fabrics. "
                            "It helps reduce ironing time for weekly clothing care."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1616628182509-6de0470f6f84",
                        "product_url": "https://kaspi.kz/shop/p/philips-gc4537-70-102894551/",
                        "count": 34,
                        "is_active": True,
                    },
                    {
                        "name": "Tefal KO8518 Electric Kettle 1.7L",
                        "price": 26990,
                        "description": (
                            "Tefal electric kettle boils water quickly and offers easy one-button operation. "
                            "Its 1.7-liter capacity is enough for tea or coffee for several people. "
                            "The design is practical for daily use at home or in the office."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1570222094114-d054a817e56b",
                        "product_url": "https://kaspi.kz/shop/p/tefal-ko8518-1-7l-103390414/",
                        "count": 22,
                        "is_active": True,
                    },
                ],
            },
            {
                "name": "TV & Entertainment",
                "products": [
                    {
                        "name": "Samsung UE55CU7100UXCE 55-inch 4K TV",
                        "price": 289990,
                        "description": (
                            "Samsung 55-inch 4K TV provides sharp detail for movies, sports, and streaming apps. "
                            "The smart interface is simple to navigate with quick access to popular platforms. "
                            "It is a strong centerpiece for a modern living room setup."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1593784991095-a205069470b6",
                        "product_url": "https://kaspi.kz/shop/p/samsung-ue55cu7100uxce-55-111273456/",
                        "count": 10,
                        "is_active": True,
                    },
                    {
                        "name": "LG 43UR78006LK 43-inch 4K Smart TV",
                        "price": 214990,
                        "description": (
                            "LG 43-inch 4K TV is a compact option for bedrooms and smaller halls. "
                            "Color reproduction is balanced and motion remains smooth in regular content. "
                            "The smart features make streaming and casting straightforward."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1461151304267-38535e780c79",
                        "product_url": "https://kaspi.kz/shop/p/lg-43ur78006lk-43-112782004/",
                        "count": 15,
                        "is_active": True,
                    },
                    {
                        "name": "Sony PlayStation 5 Slim 1TB",
                        "price": 339990,
                        "description": (
                            "PlayStation 5 Slim delivers fast loading and high-fidelity visuals in new titles. "
                            "The controller feedback adds immersion for action and sports games. "
                            "It is ideal for players who want current-gen performance at home."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db",
                        "product_url": "https://kaspi.kz/shop/p/sony-playstation-5-slim-1tb-117334812/",
                        "count": 8,
                        "is_active": True,
                    },
                    {
                        "name": "JBL Bar 2.1 Deep Bass Soundbar",
                        "price": 159990,
                        "description": (
                            "JBL Bar 2.1 adds strong low-frequency output for movies and live concerts. "
                            "Dialog remains clear while the subwoofer delivers punchy bass. "
                            "It is an easy upgrade for TV audio without a complex setup."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d",
                        "product_url": "https://kaspi.kz/shop/p/jbl-bar-2-1-deep-bass-104712399/",
                        "count": 16,
                        "is_active": True,
                    },
                    {
                        "name": "Xiaomi Mi Box S 2nd Gen",
                        "price": 37990,
                        "description": (
                            "Mi Box S turns a regular TV into a smart streaming device in minutes. "
                            "It supports major apps and voice search for quick content access. "
                            "The device is useful when you want affordable smart TV features."
                        ),
                        "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1",
                        "product_url": "https://kaspi.kz/shop/p/xiaomi-mi-box-s-2nd-gen-116990451/",
                        "count": 40,
                        "is_active": True,
                    },
                ],
            },
        ]

        Product.objects.all().delete()
        Category.objects.all().delete()

        created_categories = 0
        created_products = 0

        for category_data in catalog:
            category = Category.objects.create(name=category_data["name"])
            created_categories += 1

            for product_data in category_data["products"]:
                Product.objects.create(category=category, **product_data)
                created_products += 1

        self.stdout.write(self.style.SUCCESS("Seed completed successfully."))
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {created_categories} categories and {created_products} products."
            )
        )
