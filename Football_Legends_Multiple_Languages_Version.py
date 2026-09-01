import os
import streamlit as st
from PIL import Image, ImageOps, ImageDraw

st.set_page_config(
    page_title="Football Legends",
    page_icon="FIFA F.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- LANGUAGE SELECTOR ----------------
# 15 widely spoken languages with one-click switching.

LANGUAGES = {
    "🇬🇧 English": "en",
    "🇨🇳 中文 (Chinese)": "zh",
    "🇮🇳 हिन्दी (Hindi)": "hi",
    "🇪🇸 Español": "es",
    "🇫🇷 Français": "fr",
    "🇸🇦 العربية (Arabic)": "ar",
    "🇧🇩 বাংলা (Bengali)": "bn",
    "🇵🇹 Português": "pt",
    "🇷🇺 Русский (Russian)": "ru",
    "🇵🇰 اردو (Urdu)": "ur",
    "🇮🇩 Bahasa Indonesia": "id",
    "🇩🇪 Deutsch": "de",
    "🇯🇵 日本語 (Japanese)": "ja",
    "🇳🇬 Yoruba": "yo",
    "🇮🇹 Italiano": "it",
}

LANGUAGE_TEXT = {
    "en": {
        "title": "FOOTBALL LEGENDS",
        "search": "🔎 Search for a football legend",
        "filter": "Filter legends",
        "all": "All",
        "highlights": "🏆 Career Highlights",
        "story": "📖 LIFE & CAREER",
        "book": "📚 FOOTBALL HEROES BOOK",
        "physical": "If you want a physical copy, click the link below:",
        "view_book": "📖 VIEW THE BOOK",
        "explore": "🌍 EXPLORE FOOTBALL",
        "language": "🌐 Language",
    },
    "es": {
        "title": "LEYENDAS DEL FÚTBOL",
        "search": "{T["search"]}",
        "filter": "{T["filter"]}",
        "all": {"Todas"},
        "highlights": "{T["highlights"]}",
        "story": "{T["story"]}",
        "book": "{T["book"]}",
        "physical": "{T["physical"]}",
        "view_book": "{T["view_book"]}",
        "explore": "{T["explore"]}",
        "language": "🌐 Idioma",
    },
    "zh": {
        "title": "足球传奇",
        "search": "🔎 搜索足球传奇人物",
        "filter": "筛选传奇",
        "all": "全部",
        "highlights": "🏆 职业生涯亮点",
        "story": "📖 生涯故事",
        "book": "📚 足球英雄书籍",
        "physical": "如果你想购买实体书，请点击下面的链接：",
        "view_book": "📖 查看书籍",
        "explore": "🌍 探索足球",
        "language": "🌐 语言",
    },
    "hi": {
        "title": "फुटबॉल के दिग्गज",
        "search": "🔎 किसी फुटबॉल दिग्गज को खोजें",
        "filter": "दिग्गजों को फ़िल्टर करें",
        "all": "सभी",
        "highlights": "🏆 करियर की मुख्य उपलब्धियाँ",
        "story": "📖 जीवन और करियर",
        "book": "📚 फुटबॉल हीरोज़ पुस्तक",
        "physical": "अगर आप भौतिक प्रति चाहते हैं, तो नीचे दिए लिंक पर क्लिक करें:",
        "view_book": "📖 पुस्तक देखें",
        "explore": "🌍 फुटबॉल देखें",
        "language": "🌐 भाषा",
    },
    "fr": {
        "title": "LÉGENDES DU FOOTBALL",
        "search": "🔎 Rechercher une légende du football",
        "filter": "Filtrer les légendes",
        "all": "Toutes",
        "highlights": "🏆 Faits marquants de la carrière",
        "story": "📖 VIE ET CARRIÈRE",
        "book": "📚 LIVRE DES HÉROS DU FOOTBALL",
        "physical": "Si vous voulez un exemplaire physique, cliquez sur le lien ci-dessous :",
        "view_book": "📖 VOIR LE LIVRE",
        "explore": "🌍 EXPLORER LE FOOTBALL",
        "language": "🌐 Langue",
    },
    "de": {
        "title": "FUSSBALLLEGENDEN",
        "search": "🔎 Eine Fußballlegende suchen",
        "filter": "Legenden filtern",
        "all": "Alle",
        "highlights": "🏆 Karriere-Highlights",
        "story": "📖 LEBEN & KARRIERE",
        "book": "📚 FUSSBALLHELDEN-BUCH",
        "physical": "Wenn du ein gedrucktes Exemplar möchtest, klicke auf den Link unten:",
        "view_book": "📖 BUCH ANSEHEN",
        "explore": "🌍 FUSSBALL ENTDECKEN",
        "language": "🌐 Sprache",
    },
    "it": {
        "title": "LEGGENDE DEL CALCIO",
        "search": "🔎 Cerca una leggenda del calcio",
        "filter": "Filtra le leggende",
        "all": "Tutte",
        "highlights": "🏆 Momenti principali della carriera",
        "story": "📖 VITA E CARRIERA",
        "book": "📚 LIBRO DEGLI EROI DEL CALCIO",
        "physical": "Se vuoi una copia fisica, clicca sul link qui sotto:",
        "view_book": "📖 VEDI IL LIBRO",
        "explore": "🌍 ESPLORA IL CALCIO",
        "language": "🌐 Lingua",
    },
    "pt": {
        "title": "LENDAS DO FUTEBOL",
        "search": "🔎 Procurar uma lenda do futebol",
        "filter": "Filtrar lendas",
        "all": "Todas",
        "highlights": "🏆 Destaques da carreira",
        "story": "📖 VIDA E CARREIRA",
        "book": "📚 LIVRO DOS HERÓIS DO FUTEBOL",
        "physical": "Se quiser uma cópia física, clique no link abaixo:",
        "view_book": "📖 VER O LIVRO",
        "explore": "🌍 EXPLORAR O FUTEBOL",
        "language": "🌐 Idioma",
    },
    "ru": {
        "title": "ФУТБОЛЬНЫЕ ЛЕГЕНДЫ",
        "search": "🔎 Найти футбольную легенду",
        "filter": "Фильтр легенд",
        "all": "Все",
        "highlights": "🏆 Главные достижения карьеры",
        "story": "📖 ЖИЗНЬ И КАРЬЕРА",
        "book": "📚 КНИГА О ФУТБОЛЬНЫХ ГЕРОЯХ",
        "physical": "Если вы хотите печатную копию, нажмите на ссылку ниже:",
        "view_book": "📖 ПОСМОТРЕТЬ КНИГУ",
        "explore": "🌍 ИССЛЕДОВАТЬ ФУТБОЛ",
        "language": "🌐 Язык",
    },
    "ar": {
        "title": "أساطير كرة القدم",
        "search": "🔎 ابحث عن أسطورة كرة قدم",
        "filter": "تصفية الأساطير",
        "all": "الكل",
        "highlights": "🏆 أبرز محطات المسيرة",
        "story": "📖 الحياة والمسيرة",
        "book": "📚 كتاب أبطال كرة القدم",
        "physical": "إذا كنت تريد نسخة ورقية، اضغط على الرابط أدناه:",
        "view_book": "📖 عرض الكتاب",
        "explore": "🌍 استكشف كرة القدم",
        "language": "🌐 اللغة",
    },
    "bn": {
        "title": "ফুটবল কিংবদন্তি",
        "search": "🔎 একজন ফুটবল কিংবদন্তি খুঁজুন",
        "filter": "কিংবদন্তি ফিল্টার করুন",
        "all": "সব",
        "highlights": "🏆 ক্যারিয়ারের প্রধান অর্জন",
        "story": "📖 জীবন ও ক্যারিয়ার",
        "book": "📚 ফুটবল হিরোস বই",
        "physical": "আপনি যদি মুদ্রিত কপি চান, নিচের লিঙ্কে ক্লিক করুন:",
        "view_book": "📖 বই দেখুন",
        "explore": "🌍 ফুটবল অন্বেষণ করুন",
        "language": "🌐 ভাষা",
    },
    "id": {
        "title": "LEGENDA SEPAK BOLA",
        "search": "🔎 Cari legenda sepak bola",
        "filter": "Filter legenda",
        "all": "Semua",
        "highlights": "🏆 Sorotan Karier",
        "story": "📖 KEHIDUPAN & KARIER",
        "book": "📚 BUKU PAHLAWAN SEPAK BOLA",
        "physical": "Jika Anda ingin salinan fisik, klik tautan di bawah:",
        "view_book": "📖 LIHAT BUKU",
        "explore": "🌍 JELAJAHI SEPAK BOLA",
        "language": "🌐 Bahasa",
    },
    "ja": {
        "title": "サッカーのレジェンド",
        "search": "🔎 サッカーのレジェンドを検索",
        "filter": "レジェンドを絞り込む",
        "all": "すべて",
        "highlights": "🏆 キャリアの主な実績",
        "story": "📖 生涯とキャリア",
        "book": "📚 サッカーヒーローズの本",
        "physical": "紙の本が欲しい場合は、下のリンクをクリックしてください：",
        "view_book": "📖 本を見る",
        "explore": "🌍 サッカーを探索",
        "language": "🌐 言語",
    },
    "ur": {
        "title": "فٹ بال کے لیجنڈز",
        "search": "🔎 فٹ بال کے لیجنڈ کو تلاش کریں",
        "filter": "لیجنڈز کو فلٹر کریں",
        "all": "سب",
        "highlights": "🏆 کیریئر کی نمایاں کامیابیاں",
        "story": "📖 زندگی اور کیریئر",
        "book": "📚 فٹ بال ہیروز کی کتاب",
        "physical": "اگر آپ طباعت شدہ کتاب چاہتے ہیں تو نیچے دیے گئے لنک پر کلک کریں:",
        "view_book": "📖 کتاب دیکھیں",
        "explore": "🌍 فٹ بال دریافت کریں",
        "language": "🌐 زبان",
    },
    "yo": {
        "title": "ÀWỌN ÀLÀGBÀ BỌ́Ọ̀LÙ FÚTÙBỌ̀LÙ",
        "search": "🔎 Wa àgbà bọ́ọ̀lù fútùbòlù",
        "filter": "Ṣàlẹ̀ àwọn àlàgbà",
        "all": "Gbogbo",
        "highlights": "🏆 Àwọn àṣeyọrí pàtàkì",
        "story": "📖 ÌGBÉSÍ AYÉ & IṢẸ́",
        "book": "📚 ÌWÉ ÀWỌN AKỌNI FÚTÙBỌ̀LÙ",
        "physical": "Tí o bá fẹ́ ẹ̀dà tí a tẹ̀, tẹ ìjápọ̀ tó wà nísàlẹ̀:",
        "view_book": "📖 WO ÌWÉ",
        "explore": "🌍 ṢÀWÁRÍ FÚTÙBỌ̀LÙ",
        "language": "🌐 Èdè",
    },
}

if "language" not in st.session_state:
    st.session_state["language"] = "es"

# Sidebar selector works reliably across Streamlit versions.
with st.sidebar:
    selected_language = st.selectbox(
        "🌐 Language / Idioma",
        list(LANGUAGES.keys()),
        index=list(LANGUAGES.values()).index(st.session_state["language"])
    )
    st.session_state["language"] = LANGUAGES[selected_language]

T = LANGUAGE_TEXT[st.session_state["language"]]

FIFA_BASE = "https://www.fifa.com"

FIFA_LINKS = {
    "Inicio": FIFA_BASE + "/en",
    "Noticias": FIFA_BASE + "/en/news",
    "Torneos": FIFA_BASE + "/en/tournaments",
    "Partidos y estadísticas": FIFA_BASE + "/en/match-centre",
    "Clasificaciones": FIFA_BASE + "/en/rankings",
    "Entradas": FIFA_BASE + "/en/tickets",
    "Dentro de FIFA": FIFA_BASE + "/en/inside-fifa",
    "Jugar": FIFA_BASE + "/en/games"
}

# ---------------- CSS ----------------

st.markdown(f"""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 1600px;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(0,91,187,.65), transparent 28%),
        radial-gradient(circle at 90% 90%, rgba(0,47,108,.8), transparent 35%),
        linear-gradient(135deg, #001B44, #003B88, #005A93, #002D72);
    background-attachment: fixed;
}

.fifa-top {
    background: white;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 35px;
    margin: 0 -2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,.25);
}

.fifa-logo {
    color: #005A93;
    font-family: Arial, sans-serif;
    font-size: 38px;
    font-weight: 900;
    letter-spacing: 3px;
}

.fifa-sub {
    color: #555;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 1px;
}

.fifa-nav {
    background: #005A93;
    min-height: 55px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 28px;
    flex-wrap: wrap;
    padding: 8px 15px;
    margin: 0 -2rem 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,.3);
}

.fifa-nav a {
    color: white !important;
    text-decoration: none !important;
    font-weight: bold;
    font-size: 14px;
}

.fifa-nav a:hover {
    color: #d9eaff !important;
}

.hero {
    background: linear-gradient(100deg, rgba(0,20,60,.95), rgba(0,87,184,.7));
    border-radius: 25px;
    padding: 40px;
    margin-bottom: 25px;
    border: 1px solid rgba(255,255,255,.15);
    box-shadow: 0 12px 40px rgba(0,0,0,.35);
}

.hero-title {
    color: white;
    font-size: 50px;
    font-weight: 900;
}

.hero-text {
    color: #d9eaff;
    font-size: 20px;
}

.section-title {
    color: white;
    font-size: 30px;
    font-weight: 900;
    margin-top: 30px;
    margin-bottom: 15px;
}

.info-card {
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 18px;
    padding: 22px;
    min-height: 145px;
    box-shadow: 0 8px 25px rgba(0,0,0,.20);
}

.info-card h3, .info-card p {
    color: white !important;
}

.info-card p {
    color: #dcecff !important;
}

div.stButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,.30);
    background: rgba(255,255,255,.10);
    color: white;
    font-weight: 800;
}

div.stButton > button:hover {
    background: white;
    color: #005A93;
}

.stat-box {
    background: rgba(255,255,255,.11);
    border-left: 4px solid white;
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 10px;
    color: white;
    font-weight: bold;
}

.bio-box {
    background: rgba(0,0,0,.23);
    border-radius: 22px;
    padding: 30px;
    margin-top: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,.25);
}

.book-box {
    background: linear-gradient(135deg, rgba(255,255,255,.15), rgba(255,255,255,.06));
    border-radius: 22px;
    padding: 30px;
    margin-top: 30px;
    text-align: center;
    border: 1px solid rgba(255,255,255,.2);
}

.book-box h2, .book-box p {
    color: white !important;
}

.disclaimer, .footer {
    text-align: center;
    color: #005A93;
    padding: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FIFA HEADER ----------------

st.markdown(f"""
<div class="fifa-top">
    <div class="fifa-logo">FIFA</div>
    <div class="fifa-sub">LEYENDAS DEL FÚTBOL • PROYECTO DE FANS NO OFICIAL</div>
</div>
""", unsafe_allow_html=True)

nav_html = '<div class="fifa-nav">'
for label, url in FIFA_LINKS.items():
    nav_html += f'<a href="{url}" target="_blank">{label.upper()}</a>'
nav_html += "</div>"
st.markdown(nav_html, unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown(f"""
<div class="hero">
    <div class="hero-title">⚽ {T["title"]}</div>
    <div class="hero-text">
        Descubre las historias, carreras, trofeos y récords
        de los mejores futbolistas.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- PLAYERS ----------------

players = {
    "Pelé": {
        "image": "Pele.jpg",
        "country": "🇧🇷 Brasil",
        "life": "1940 – 2022",
        "category": "Iconos del Mundial",
        "stats": ["3 Copas Mundiales de la FIFA", "Leyenda de Brasil", "Santos legend", "1,000+ career goals"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Pelé, cuyo nombre era Edson Arantes do Nascimento, creció en Brasil y desarrolló su talento futbolístico desde muy joven. Se unió al Santos siendo adolescente y rápidamente se convirtió en una estrella mundial.

Ganó la Copa Mundial de la FIFA con Brasil en 1958, 1962 y 1970. Con Santos conquistó importantes títulos nacionales e internacionales y más tarde jugó para el New York Cosmos, ayudando a popularizar el fútbol en Estados Unidos.

Después de retirarse se convirtió en embajador mundial del fútbol. Murió en 2022 y sigue siendo el único jugador que ha ganado tres Copas Mundiales."""
    },

    "Maradona": {
        "image": "Maradona.AVIF",
        "country": "🇦🇷 Argentina",
        "life": "1960 – 2020",
        "category": "Iconos del Mundial",
        "stats": ["1986 FIFA Campeón del Mundial", "Capitán de Argentina", "Napoli legend", "Balón de Oro del Mundial"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Diego Maradona creció en Villa Fiorito, Argentina, y desde niño destacó por su extraordinario talento. Jugó para Argentinos Juniors y Boca Juniors antes de marcharse a Europa.

En Napoli se convirtió en un ídolo y ayudó al club a conquistar la Serie A. Su mayor momento llegó en la Copa Mundial de 1986, cuando como capitán llevó a Argentina al título y marcó dos de los goles más famosos de la historia contra Inglaterra.

También llevó a Argentina a la final del Mundial de 1990. Después de retirarse trabajó como entrenador y siguió siendo una de las figuras más influyentes del fútbol hasta su muerte en 2020."""
    },

    "Lionel Messi": {
        "image": "Messi.jpg",
        "country": "🇦🇷 Argentina",
        "life": "Born 1987",
        "category": "Leyendas modernas",
        "stats": ["2022 FIFA Campeón del Mundial", "8 Balones de Oro", "Leyenda del Barcelona", "850+ senior goals"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Lionel Messi nació en Rosario, Argentina. Desde niño mostró un talento extraordinario y a los 13 años se trasladó a España para incorporarse a la academia del Barcelona.

En La Masia se convirtió en una leyenda del club gracias a su regate, visión, pases y capacidad goleadora. Ganó numerosos títulos de La Liga y de la Champions League.

Con Argentina ganó la Copa América en 2021 y, en 2022, capitaneó a su selección hasta el título de la Copa Mundial en Catar, además de recibir el Balón de Oro del torneo. Después jugó para Paris Saint-Germain y se incorporó al Inter Miami."""
    },

    "Cristiano Ronaldo": {
        "image": "Ronaldo.AVIF",
        "country": "🇵🇹 Portugal",
        "life": "Born 1985",
        "category": "Leyendas modernas",
        "stats": ["5 Balones de Oro", "Portugal Campeón de Europa", "5 títulos de Champions League", "900+ senior goals"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Cristiano Ronaldo nació en Funchal, Madeira, Portugal. Desde pequeño estuvo dedicado al fútbol y pasó por la academia del Sporting CP antes de convertirse en profesional.

Manchester United lo fichó siendo adolescente y allí se transformó en una de las mayores estrellas del mundo. En 2009 pasó al Real Madrid, donde se convirtió en máximo goleador histórico del club y ganó varias Champions League.

Con Portugal ganó la Euro 2016 y posteriormente la UEFA Nations League. También jugó para Juventus y regresó a Manchester United antes de continuar su carrera en Al Nassr. Su trayectoria destaca por sus goles, atletismo, disciplina y longevidad."""
    },

    "Ronaldinho": {
        "image": "Ronaldinho.PNG",
        "country": "🇧🇷 Brasil",
        "life": "Born 1980",
        "category": "Leyendas clásicas",
        "stats": ["2002 FIFA Campeón del Mundial", "Ganador del Balón de Oro", "Leyenda del Barcelona", "Copa Libertadores winner"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Ronaldinho creció en Porto Alegre, Brasil, en una familia apasionada por el fútbol. Se hizo famoso por sus regates, trucos, creatividad y alegría sobre el campo.

Comenzó profesionalmente en Grêmio y después triunfó en Europa, especialmente con Barcelona, donde ganó La Liga, la Champions League y el Balón de Oro. Con Brasil formó parte del equipo campeón del Mundial de 2002.

Más tarde jugó para AC Milan y otros clubes, incluido Atlético Mineiro, con el que ganó la Copa Libertadores. Se retiró en 2018 y sigue siendo uno de los futbolistas más reconocibles de la historia."""
    },

    "Zinedine Zidane": {
        "image": "Zidane.jpg",
        "country": "🇫🇷 Francia",
        "life": "Born 1972",
        "category": "Leyendas clásicas",
        "stats": ["1998 FIFA Campeón del Mundial", "Ganador del Balón de Oro", "Campeón de la Champions League", "Leyenda del Real Madrid"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Zinedine Zidane creció en Marsella, Francia, y se convirtió en un elegante centrocampista ofensivo conocido por su control, visión y técnica.

Jugó para Bordeaux y Juventus antes de llegar al Real Madrid. En 1998 ayudó a Francia a ganar el Mundial y marcó dos goles en la final contra Brasil.

Después ganó la Champions League de 2002 con el Real Madrid y posteriormente tuvo una exitosa carrera como entrenador, conquistando tres Champions League consecutivas con el club entre 2016 y 2018."""
    },

    "Ronaldo Nazário": {
        "image": "Ronaldo Nazario.jpg",
        "country": "🇧🇷 Brasil",
        "life": "Born 1976",
        "category": "Leyendas clásicas",
        "stats": ["2 Copas Mundiales de la FIFA", "2 Balones de Oro", "Leyenda de Brasil", "2002 World Cup top scorer"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Ronaldo Nazário creció en Brasil y rápidamente fue considerado uno de los delanteros jóvenes más prometedores del mundo. Jugó en Europa para PSV, Barcelona e Inter antes de llegar al Real Madrid.

Era conocido por su aceleración explosiva, regate y definición. En 2002 regresó con fuerza después de graves lesiones y lideró a Brasil hasta el título mundial, marcando dos goles en la final contra Alemania.

También ganó grandes trofeos con Real Madrid y AC Milan y es recordado como uno de los delanteros naturales más talentosos de todos los tiempos."""
    },

    "Neymar": {
        "image": "Neymar.jpg",
        "country": "🇧🇷 Brasil",
        "life": "Born 1992",
        "category": "Leyendas modernas",
        "stats": ["Brasil international star", "Leyenda del Barcelona", "2015 Campeón de la Champions League", "Olympic gold medal"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Neymar creció en Brasil y se hizo famoso como joven estrella del Santos gracias a su regate, creatividad y habilidad.

En Barcelona formó un tridente histórico con Lionel Messi y Luis Suárez y ganó importantes títulos, incluida la Champions League de 2015. Después pasó al Paris Saint-Germain en uno de los fichajes más importantes del fútbol.

Con Brasil se convirtió en una de sus figuras principales y en 2016 ayudó a la selección a ganar el oro olímpico en Río de Janeiro."""
    },

    "Kylian Mbappé": {
        "image": "Mbappe.jpg",
        "country": "🇫🇷 Francia",
        "life": "Born 1998",
        "category": "Leyendas modernas",
        "stats": ["2018 FIFA Campeón del Mundial", "2022 Bota de Oro del Mundial", "Francia international", "Real Madrid star"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Kylian Mbappé creció cerca de París y destacó como prodigio del fútbol. Debutó con el primer equipo del Monaco siendo adolescente y pronto llamó la atención de toda Europa.

Después pasó al Paris Saint-Germain y se convirtió en uno de sus principales goleadores. En el Mundial de 2018 ayudó a Francia a conquistar el título y marcó en la final.

En el Mundial de 2022 marcó un hat-trick en la final contra Argentina y ganó la Bota de Oro. Posteriormente se incorporó al Real Madrid."""
    },

    "Erling Haaland": {
        "image": "Haaland.jpg",
        "country": "🇳🇴 Noruega",
        "life": "Born 2000",
        "category": "Leyendas modernas",
        "stats": ["Campeón de la Champions League", "Manchester City star", "Premier League record breaker", "Noruega international"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Erling Haaland nació en Leeds, Inglaterra, y creció en Noruega. Se desarrolló como un delantero potente y extremadamente goleador.

Destacó con Molde y Red Bull Salzburg antes de brillar en Borussia Dortmund. En 2022 llegó al Manchester City y ayudó al club a conquistar la Premier League y la Champions League.

Su combinación de tamaño, velocidad y definición lo convirtió en uno de los delanteros más temidos de su generación."""
    },

    "Robert Lewandowski": {
        "image": "Robert Lewandowski.jpg",
        "country": "🇵🇱 Polonia",
        "life": "Born 1988",
        "category": "Leyendas modernas",
        "stats": ["Campeón de la Champions League", "Bayern Munich legend", "Barcelona striker", "Polonia captain"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Robert Lewandowski creció en Polonia dentro de una familia deportiva. Se desarrolló en el fútbol polaco antes de trasladarse al Borussia Dortmund.

En 2014 fichó por el Bayern Múnich y se convirtió en uno de los goleadores más constantes del mundo. Ganó numerosos títulos de Bundesliga y la Champions League de 2020.

Con Polonia se convirtió en capitán y principal referente ofensivo, destacando por su movimiento, definición y regularidad."""
    },

    "Zlatan Ibrahimović": {
        "image": "Zlatan.jpg",
        "country": "🇸🇪 Suecia",
        "life": "Born 1981",
        "category": "Leyendas modernas",
        "stats": ["Suecia legend", "Multiple league champion", "Ajax, Inter, Milan & PSG star", "Iconic football personality"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Zlatan Ibrahimović creció en Malmö, Suecia, y desarrolló una combinación poco habitual de potencia, técnica y confianza.

Jugó para Malmö, Ajax, Juventus, Inter, Barcelona, AC Milan, Paris Saint-Germain y Manchester United, entre otros clubes. Marcó goles espectaculares y ganó títulos de liga en varios países.

Regresó al AC Milan en la última etapa de su carrera y continuó jugando al máximo nivel hasta pasados los cuarenta años."""
    },

    "Luís Figo": {
        "image": "Luis Figo.jpg",
        "country": "🇵🇹 Portugal",
        "life": "Born 1972",
        "category": "Leyendas clásicas",
        "stats": ["Ganador del Balón de Oro", "Capitán de Portugal", "Barcelona star", "Leyenda del Real Madrid"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Luís Figo creció en Portugal y se convirtió en uno de los extremos más talentosos de Europa. Pasó por Sporting CP antes de convertirse en estrella del Barcelona.

Su fichaje por el Real Madrid, directamente desde el gran rival, fue uno de los traspasos más polémicos del fútbol moderno. Con el Real Madrid formó parte de la era de los Galácticos y ganó el Balón de Oro en 2000.

Con Portugal fue capitán y líder de la llamada Generación de Oro."""
    },

    "Jude Bellingham": {
        "image": "Jude Bellingham.jpg",
        "country": "🏴 Inglaterra",
        "life": "Born 2003",
        "category": "Leyendas modernas",
        "stats": ["Inglaterra international", "Real Madrid star", "Campeón de la Champions League", "Young midfield superstar"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Jude Bellingham creció en Birmingham y entró en la academia del Birmingham City siendo muy joven. Se convirtió en el jugador más joven en debutar con el primer equipo del club antes de trasladarse al Borussia Dortmund.

En Alemania se desarrolló como centrocampista y disputó la Champions League. Después fichó por el Real Madrid y rápidamente se convirtió en una de sus grandes figuras jóvenes.

Con Inglaterra participó en el Mundial de 2022 siendo todavía adolescente y se consolidó como una de las grandes promesas del fútbol mundial."""
    },

    "Johan Cruyff": {
        "image": "Cruyff.jpg", "country": "🇳🇱 Países Bajos", "life": "1947 – 2016",
        "category": "Leyendas clásicas",
        "stats": ["3 Balones de Oro", "Ajax legend", "Leyenda del Barcelona", "Total Football icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Johan Cruyff fue una figura central de la era del Fútbol Total. Brilló con Ajax y Barcelona y más tarde se convirtió en un entrenador enormemente influyente.

Con Países Bajos lideró al famoso equipo de 1974 hasta la final del Mundial. Su inteligencia, movilidad y técnica cambiaron la manera de entender el fútbol y dejaron una influencia duradera en generaciones posteriores."""
    },
    "Franz Beckenbauer": {
        "image": "Beckenbauer.AVIF", "country": "🇩🇪 Alemania", "life": "1945 – 2024",
        "category": "Leyendas clásicas",
        "stats": ["2 Balones de Oro", "1974 Campeón del Mundial", "Bayern Munich legend", "World Cup-winning coach"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Franz Beckenbauer revolucionó la posición de líbero. Se convirtió en una leyenda del Bayern Múnich y capitaneó a Alemania Occidental hasta ganar el Mundial de 1974.

Más tarde entrenó a Alemania Occidental y ganó el Mundial de 1990. Es una de las pocas personas que conquistaron la Copa Mundial como jugador y como entrenador."""
    },
    "Michel Platini": {
        "image": "Platini.jpg", "country": "🇫🇷 Francia", "life": "Born 1955",
        "category": "Leyendas clásicas",
        "stats": ["3 consecutive Balones de Oro", "1984 European Championship winner", "Juventus legend", "Capitán de Francia"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Michel Platini fue uno de los grandes centrocampistas de Francia. Brilló con Nancy, Saint-Étienne y Juventus, destacando por sus pases, lanzamientos de falta y goles.

Ganó tres Balones de Oro consecutivos y lideró a Francia al título de la Eurocopa de 1984."""
    },
    "Ferenc Puskás": {
        "image": "Puskas.jpg", "country": "🇭🇺 Hungary / 🇪🇸 España", "life": "1927 – 2006",
        "category": "Leyendas clásicas",
        "stats": ["Hungary legend", "Leyenda del Real Madrid", "Olympic champion", "Campeón de la Copa de Europa"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Ferenc Puskás fue capitán del legendario equipo de Hungría y uno de los grandes goleadores zurdos de la historia.

Ayudó a Hungría a ganar el oro olímpico y posteriormente se convirtió en una leyenda del Real Madrid, donde conquistó grandes títulos nacionales y europeos."""
    },
    "Garrincha": {
        "image": "Garrincha.jpg", "country": "🇧🇷 Brasil", "life": "1933 – 1983",
        "category": "Iconos del Mundial",
        "stats": ["2 Copas Mundiales de la FIFA", "Leyenda de Brasil", "1958 Campeón del Mundial", "1962 World Cup star"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Garrincha se hizo famoso por sus regates extraordinarios y su capacidad para superar defensores. Fue una pieza fundamental de Brasil en los Mundiales de 1958 y 1962.

En 1962 tuvo un papel especialmente importante cuando Pelé sufrió una lesión. Su estilo imprevisible y divertido lo convirtió en uno de los extremos más queridos de la historia."""
    },
    "George Best": {
        "image": "George Best.jpg", "country": "🇬🇧 Irlanda del Norte", "life": "1946 – 2005",
        "category": "Leyendas clásicas",
        "stats": ["Campeón de la Copa de Europa", "Manchester United legend", "Ganador del Balón de Oro", "Irlanda del Norte icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """George Best creció en Belfast y se convirtió en una superestrella del Manchester United. Su velocidad, regate y talento ayudaron al club a ganar la Copa de Europa en 1968.

Ese mismo año ganó el Balón de Oro y quedó consagrado como uno de los jugadores más talentosos de su generación."""
    },
    "Paolo Maldini": {
        "image": "Maldini.jpg", "country": "🇮🇹 Italia", "life": "Born 1968",
        "category": "Leyendas clásicas",
        "stats": ["5 European Cups/Champions Leagues", "AC Milan legend", "Capitán de Italia", "Defensive icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Paolo Maldini pasó toda su carrera de clubes en el AC Milan y se convirtió en uno de los mejores defensores de la historia.

Ganó numerosos títulos nacionales y cinco Copas de Europa o Champions League. También fue capitán de Italia y disputó cuatro Mundiales, destacando por su inteligencia, técnica y liderazgo."""
    },
    "Xavi Hernández": {
        "image": "Xavi.jpg", "country": "🇪🇸 España", "life": "Born 1980",
        "category": "Leyendas modernas",
        "stats": ["2010 FIFA Campeón del Mundial", "2 European Championships", "Leyenda del Barcelona", "4 títulos de Champions League"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Xavi se formó en La Masia y se convirtió en uno de los centrocampistas más influyentes de la era moderna. Su pase, movimiento y control fueron fundamentales para Barcelona y para la generación dorada de España.

Con España ganó la Eurocopa de 2008 y 2012 y el Mundial de 2010. Con Barcelona ganó múltiples títulos nacionales y europeos."""
    },
    "Andrés Iniesta": {
        "image": "Iniesta.jpg", "country": "🇪🇸 España", "life": "Born 1984",
        "category": "Leyendas modernas",
        "stats": ["2010 FIFA Campeón del Mundial", "2 European Championships", "Leyenda del Barcelona", "World Cup final goalscorer"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Andrés Iniesta llegó a la academia del Barcelona siendo niño y se convirtió en uno de los centrocampistas más elegantes del mundo.

Ganó numerosos títulos con Barcelona. Con España ganó las Eurocopas de 2008 y 2012 y el Mundial de 2010, marcando el gol decisivo en la final."""
    },
    "Gianluigi Buffon": {
        "image": "Buffon.jpg", "country": "🇮🇹 Italia", "life": "Born 1978",
        "category": "Leyendas modernas",
        "stats": ["2006 FIFA Campeón del Mundial", "Juventus legend", "Capitán de Italia", "Goalkeeping icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Gianluigi Buffon está considerado uno de los mejores porteros de la historia. Se convirtió en una leyenda de la Juventus y ganó numerosos títulos de Serie A.

Fue el portero titular de Italia durante el Mundial de 2006, que la selección italiana conquistó. Su longevidad, liderazgo y capacidad para detener disparos marcaron una época."""
    }
,

    "Lev Yashin": {
        "image": "Yashin.jpg", "country": "🇷🇺 Unión Soviética", "life": "1929 – 1990",
        "category": "Leyendas clásicas",
        "stats": ["1963 Ballon d'Or", "1960 Campeón de Europa", "Unión Soviética legend", "Goalkeeping pioneer"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Lev Yashin, conocido como la Araña Negra, es considerado uno de los mejores porteros de todos los tiempos. Pasó toda su carrera profesional en el Dynamo de Moscú.

En 1963 ganó el Balón de Oro, siendo el único portero que ha recibido ese premio. Fue un pionero por su capacidad para dirigir la defensa y participar activamente en el juego."""
    },
    "Eusébio": {
        "image": "Eusebio.jpg", "country": "🇵🇹 Portugal", "life": "1942 – 2014",
        "category": "Leyendas clásicas",
        "stats": ["1965 Ballon d'Or", "1966 Bota de Oro del Mundial", "Benfica legend", "Portugal icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Eusébio fue la primera gran superestrella mundial del fútbol portugués. Con Benfica ganó importantes títulos nacionales y europeos.

En el Mundial de 1966 marcó nueve goles, ayudó a Portugal a llegar a semifinales y ganó la Bota de Oro del torneo."""
    },
    "Marco van Basten": {
        "image": "Van_Basten.jpg", "country": "🇳🇱 Países Bajos", "life": "Born 1964",
        "category": "Leyendas clásicas",
        "stats": ["3 Balones de Oro", "1988 Campeón de Europa", "AC Milan legend", "Euro 1988 Golden Boot"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Marco van Basten fue un delantero extraordinario que brilló con Ajax y AC Milan. Ganó tres Balones de Oro.

Con Países Bajos ganó la Eurocopa de 1988 y marcó una famosa volea en la final, uno de los goles más recordados de la historia del torneo."""
    },
    "Romário": {
        "image": "Romario.jpg", "country": "🇧🇷 Brasil", "life": "Born 1966",
        "category": "Iconos del Mundial",
        "stats": ["1994 FIFA Campeón del Mundial", "1994 Balón de Oro del Mundial", "Leyenda de Brasil", "Barcelona star"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Romário fue un brillante delantero brasileño conocido por su control cercano y su definición. Ayudó a Brasil a ganar el Mundial de 1994 y fue reconocido como uno de los mejores jugadores del torneo.

También tuvo grandes etapas en PSV y Barcelona, donde demostró su enorme capacidad goleadora."""
    },
    "Cafu": {
        "image": "Cafu.jpg", "country": "🇧🇷 Brasil", "life": "Born 1970",
        "category": "Iconos del Mundial",
        "stats": ["2 FIFA World Cup wins", "2002 World Cup captain", "Leyenda de Brasil", "AC Milan legend"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Cafu fue uno de los mejores laterales ofensivos de la historia. Disputó tres finales consecutivas de la Copa Mundial y ganó el torneo con Brasil en 1994 y 2002.

En 2002 fue capitán de Brasil en la final y se convirtió en una de las grandes figuras de la generación campeona."""
    },
    "Roberto Carlos": {
        "image": "Roberto_Carlos.jpg", "country": "🇧🇷 Brasil", "life": "Born 1973",
        "category": "Leyendas clásicas",
        "stats": ["2002 FIFA Campeón del Mundial", "3 títulos de Champions League", "Leyenda del Real Madrid", "Famous free-kick specialist"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Roberto Carlos fue uno de los laterales izquierdos ofensivos más influyentes del fútbol. Se convirtió en leyenda del Real Madrid, ganó tres Champions League y ayudó a Brasil a conquistar el Mundial de 2002.

Sus potentes disparos y lanzamientos de falta se hicieron famosos en todo el mundo."""
    },
    "Thierry Henry": {
        "image": "Henry.jpg", "country": "🇫🇷 Francia", "life": "Born 1977",
        "category": "Leyendas modernas",
        "stats": ["1998 FIFA Campeón del Mundial", "2000 Campeón de Europa", "Arsenal legend", "Premier League icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Thierry Henry pasó de ser una joven promesa del Monaco a convertirse en uno de los delanteros más peligrosos del mundo. Fue una leyenda del Arsenal y una pieza importante de Francia.

Ganó el Mundial de 1998 y la Eurocopa de 2000. Su velocidad, definición y movimientos lo convirtieron en uno de los mejores delanteros de la Premier League."""
    },
    "Didier Drogba": {
        "image": "Drogba.jpg", "country": "🇨🇮 Costa de Marfil", "life": "Born 1978",
        "category": "Leyendas modernas",
        "stats": ["4 títulos de Premier League", "Campeón de la Champions League", "Chelsea legend", "Ivory Coast captain"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Didier Drogba se convirtió en una leyenda del Chelsea después de crecer futbolísticamente en Francia. Marcó en partidos importantes y ayudó al Chelsea a ganar varios títulos, incluida la Champions League de 2012.

También fue capitán y una figura fundamental de la generación dorada de Costa de Marfil."""
    },
    "Samuel Eto'o": {
        "image": "Etoo.jpg", "country": "🇨🇲 Camerún", "life": "Born 1981",
        "category": "Leyendas modernas",
        "stats": ["3 títulos de Champions League", "Leyenda del Barcelona", "Camerún legend", "Olympic gold medal"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Samuel Eto'o fue uno de los grandes delanteros africanos. Brilló con Mallorca, Barcelona e Inter de Milán y ganó tres Champions League.

También conquistó el oro olímpico con Camerún y se convirtió en uno de los futbolistas africanos más laureados de la historia."""
    },
    "Kaká": {
        "image": "Kaka.jpg", "country": "🇧🇷 Brasil", "life": "Born 1982",
        "category": "Leyendas modernas",
        "stats": ["2007 Ballon d'Or", "2002 FIFA Campeón del Mundial", "AC Milan legend", "Campeón de la Champions League"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Kaká fue un talentoso centrocampista ofensivo brasileño que se convirtió en estrella del AC Milan. Ganó el Balón de Oro de 2007 después de ayudar al Milan a conquistar la Champions League.

También formó parte del equipo de Brasil que ganó el Mundial de 2002."""
    },
    "Andrea Pirlo": {
        "image": "Pirlo.jpg", "country": "🇮🇹 Italia", "life": "Born 1979",
        "category": "Leyendas modernas",
        "stats": ["2006 FIFA Campeón del Mundial", "2 títulos de Champions League", "Italia legend", "Midfield maestro"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Andrea Pirlo fue famoso por su calma, visión, pases y lanzamientos de falta. Ganó importantes títulos con AC Milan y Juventus.

Fue una pieza clave de Italia en el Mundial de 2006 y es recordado como uno de los mejores organizadores de juego de su generación."""
    },
    "Sergio Ramos": {
        "image": "Ramos.jpg", "country": "🇪🇸 España", "life": "Born 1986",
        "category": "Leyendas modernas",
        "stats": ["2010 FIFA Campeón del Mundial", "2 European Championships", "4 títulos de Champions League", "Real Madrid captain"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Sergio Ramos se convirtió en uno de los defensores más exitosos de su generación. Ganó numerosos trofeos con el Real Madrid y fue capitán del club.

Con España ganó la Eurocopa de 2008, el Mundial de 2010 y la Eurocopa de 2012."""
    },
    "Manuel Neuer": {
        "image": "Neuer.jpg", "country": "🇩🇪 Alemania", "life": "Born 1986",
        "category": "Leyendas modernas",
        "stats": ["2014 FIFA Campeón del Mundial", "2 títulos de Champions League", "Bayern Munich legend", "Goalkeeper revolution"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Manuel Neuer transformó el papel del portero moderno gracias a su capacidad para salir del área y participar en la construcción del juego.

Se convirtió en leyenda del Bayern Múnich y ganó múltiples títulos de Bundesliga y Champions League. Fue el portero de Alemania durante el Mundial de 2014."""
    },
    "Luka Modrić": {
        "image": "Modric.jpg", "country": "🇭🇷 Croacia", "life": "Born 1985",
        "category": "Leyendas modernas",
        "stats": ["2018 Ballon d'Or", "2018 Finalista del Mundial", "6 títulos de Champions League", "Leyenda del Real Madrid"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Luka Modrić pasó del fútbol croata a convertirse en uno de los mejores centrocampistas del mundo. Fue una figura clave del Real Madrid y ganó múltiples Champions League.

En 2018 capitaneó a Croacia hasta la final del Mundial y ganó el Balón de Oro de ese año."""
    },
    "Kevin De Bruyne": {
        "image": "De_Bruyne.jpg", "country": "🇧🇪 Bélgica", "life": "Born 1991",
        "category": "Leyendas modernas",
        "stats": ["Campeón de la Champions League", "Manchester City legend", "Campeón de la Premier League", "Bélgica star"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Kevin De Bruyne se convirtió en uno de los mejores centrocampistas creativos del fútbol moderno. Es una figura clave del Manchester City y ha ganado múltiples títulos de Premier League y la Champions League.

Su visión, pases, centros y disparos lo han convertido en uno de los mejores futbolistas de Bélgica."""
    },
    "Mohamed Salah": {
        "image": "Salah.jpg", "country": "🇪🇬 Egipto", "life": "Born 1992",
        "category": "Leyendas modernas",
        "stats": ["Campeón de la Premier League", "Campeón de la Champions League", "Liverpool legend", "Egipto captain"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Mohamed Salah pasó del fútbol egipcio a convertirse en una estrella mundial. Después de jugar en Suiza, Italia e Inglaterra, se convirtió en una leyenda del Liverpool.

Ayudó al Liverpool a ganar la Premier League y la Champions League y se consolidó como uno de los delanteros más productivos del mundo."""
    },
    "Luis Suárez": {
        "image": "Suarez.jpg", "country": "🇺🇾 Uruguay", "life": "Born 1987",
        "category": "Leyendas modernas",
        "stats": ["2011 Copa América winner", "Campeón de la Champions League", "Leyenda del Barcelona", "Uruguay icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Luis Suárez se convirtió en uno de los grandes delanteros del mundo durante sus etapas en Ajax, Liverpool, Barcelona y Atlético de Madrid.

En Barcelona formó un famoso tridente con Messi y Neymar y ganó la Champions League. Con Uruguay ganó la Copa América de 2011."""
    },
    "Karim Benzema": {
        "image": "Benzema.jpg", "country": "🇫🇷 Francia", "life": "Born 1987",
        "category": "Leyendas modernas",
        "stats": ["2022 Ballon d'Or", "5 títulos de Champions League", "Leyenda del Real Madrid", "Francia international"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Karim Benzema se convirtió en uno de los delanteros más exitosos de la historia del Real Madrid. Ganó cinco Champions League y asumió un papel protagonista en el ataque del club.

En 2022 recibió el Balón de Oro después de una temporada extraordinaria."""
    },
    "Arjen Robben": {
        "image": "Robben.jpg", "country": "🇳🇱 Países Bajos", "life": "Born 1984",
        "category": "Leyendas modernas",
        "stats": ["2013 Campeón de la Champions League", "Bayern Munich legend", "Países Bajos star", "Finalista del Mundial"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Arjen Robben fue famoso por recortar desde la banda derecha hacia su pierna izquierda. Tuvo grandes etapas en Chelsea, Real Madrid y Bayern Múnich.

Su gol decisivo en la final de la Champions League de 2013 se convirtió en uno de los momentos más famosos de la historia reciente del Bayern."""
    },
    "Frank Lampard": {
        "image": "Lampard.jpg", "country": "🏴 Inglaterra", "life": "Born 1978",
        "category": "Leyendas modernas",
        "stats": ["Campeón de la Champions League", "3 títulos de Premier League", "Chelsea legend", "Inglaterra international"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Frank Lampard se convirtió en el máximo goleador histórico del Chelsea pese a jugar como centrocampista. Ganó tres Premier League y la Champions League con el club.

Fue conocido por sus llegadas al área, pases y extraordinaria capacidad goleadora."""
    },
    "Steven Gerrard": {
        "image": "Gerrard.jpg", "country": "🏴 Inglaterra", "life": "Born 1980",
        "category": "Leyendas modernas",
        "stats": ["Campeón de la Champions League", "Liverpool captain", "2005 final hero", "Inglaterra legend"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """Steven Gerrard pasó la mayor parte de su carrera en el Liverpool y se convirtió en uno de los grandes capitanes del club.

Fue fundamental en la dramática victoria del Liverpool en la Champions League de 2005 y destacó por su liderazgo, disparos lejanos y pases."""
    },
    "David Beckham": {
        "image": "Beckham.jpg", "country": "🏴 Inglaterra", "life": "Born 1975",
        "category": "Leyendas clásicas",
        "stats": ["6 títulos de Premier League", "Campeón de la Champions League", "Capitán de Inglaterra", "Global football icon"],
        "book": "https://www.lovereading4kids.co.uk/author/Matt-Oldfield",
        "story": """David Beckham se hizo famoso por sus centros, pases y lanzamientos de falta con el Manchester United. Ganó seis títulos de Premier League y la Champions League.

Después jugó para Real Madrid, LA Galaxy, AC Milan y Paris Saint-Germain. También se convirtió en uno de los embajadores globales más reconocidos del fútbol."""
    }

}

# ---------------- FOOTBALL HUB ----------------

st.markdown('<div class="section-title">🌍 CENTRO DE FÚTBOL FIFA</div>', unsafe_allow_html=True)

hub1, hub2, hub3, hub4 = st.columns(4)

with hub1:
    st.markdown(f"""
    <div class="info-card">
        <h3>🏆 Torneos</h3>
        <p>Mundiales, competiciones femeninas, torneos juveniles y fútbol internacional.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Explorar torneos FIFA →", FIFA_LINKS["Torneos"], use_container_width=True)

with hub2:
    st.markdown(f"""
    <div class="info-card">
        <h3>📊 Partidos y estadísticas</h3>
        <p>Explora partidos, competiciones, selecciones y estadísticas de fútbol.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir centro de partidos →", FIFA_LINKS["Partidos y estadísticas"], use_container_width=True)

with hub3:
    st.markdown(f"""
    <div class="info-card">
        <h3>📰 Noticias FIFA</h3>
        <p>Explora noticias, reportajes, récords e historias del fútbol de todo el mundo.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Leer noticias FIFA →", FIFA_LINKS["Noticias"], use_container_width=True)

with hub4:
    st.markdown(f"""
    <div class="info-card">
        <h3>🌐 Clasificaciones FIFA</h3>
        <p>Consulta las clasificaciones internacionales y las selecciones nacionales.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Ver clasificaciones →", FIFA_LINKS["Clasificaciones"], use_container_width=True)

# ---------------- SEARCH / FILTER ----------------

st.markdown('<div class="section-title">⭐ BASE DE DATOS DE LEYENDAS</div>', unsafe_allow_html=True)

search = st.text_input(
    "{T["search"]}",
    placeholder="Escribe el nombre de un jugador..."
)

category = st.selectbox(
    "{T["filter"]}",
    ["Todas", "Iconos del Mundial", "Leyendas clásicas", "Leyendas modernas"]
)

filtered_players = {}

for name, data in players.items():
    search_match = search.lower() in name.lower() if search else True
    category_match = category == "Todas" or data["category"] == category

    if search_match and category_match:
        filtered_players[name] = data

if not filtered_players:
    st.warning("No se encontró ninguna leyenda del fútbol.")
else:
    names = list(filtered_players.keys())

    for start in range(0, len(names), 6):
        row_names = names[start:start + 6]
        columns = st.columns(6)

        for index, name in enumerate(row_names):
            with columns[index]:
                image_path = players[name]["image"]

                if os.path.exists(image_path):
                    try:
                        image = Image.open(image_path).convert("RGB")
                        image = ImageOps.fit(image, (180, 180))
                        mask = Image.new("L", (180, 180), 0)
                        draw = ImageDraw.Draw(mask)
                        draw.ellipse((0, 0, 180, 180), fill=255)
                        image.putalpha(mask)
                        st.image(image, width=120)
                    except Exception:
                        st.write("⚽")
                else:
                    initials = "".join(
                        word[0] for word in name.split() if word
                    )[:2]

                    st.markdown(
                        f"""
                        <div style="
                            width:120px;height:120px;border-radius:50%;
                            background:#005A93;border:4px solid white;
                            display:flex;align-items:center;justify-content:center;
                            margin:auto;color:white;font-size:32px;font-weight:bold;">
                            {initials}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                if st.button(name, key=f"legend_{name}"):
                    st.session_state["legend"] = name

# ---------------- DEFAULT PLAYER ----------------

if "legend" not in st.session_state:
    st.session_state["legend"] = "Lionel Messi"

player_name = st.session_state["legend"]
player = players[player_name]

st.markdown("---")

# ---------------- PLAYER HERO ----------------

left, right = st.columns([1.15, 1])

with left:
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-title">{player_name}</div>
            <div class="hero-text">{player["country"]}</div>
            <p style="color:#d9eaff;"><b>Época:</b> {player["life"]}</p>
            <p style="color:#d9eaff;"><b>Categoría:</b> {player["category"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### {T["highlights"]}")

    for stat in player["stats"]:
        st.markdown(
            f'<div class="stat-box">⭐ {stat}</div>',
            unsafe_allow_html=True
        )

with right:
    image_path = player["image"]

    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div style="
                height:450px;background:rgba(255,255,255,.08);
                border-radius:25px;display:flex;align-items:center;
                justify-content:center;color:white;font-size:30px;
                font-weight:bold;">
                ⚽ {player_name}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- LIFE STORY ----------------

st.markdown('<div class="section-title">{T["story"]}</div>', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="bio-box">
        <h2 style="color:white;">La historia de {player_name}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(player["story"])

# ---------------- BOOK ----------------

st.markdown('<div class="section-title">{T["book"]}</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="book-box">
        <h2>{T["physical"]}</h2>
        <p>
            El botón de abajo te lleva a una página de compra o búsqueda de libros
            de Matt Oldfield.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.link_button(
    "{T["view_book"]}",
    player["book"],
    use_container_width=True
)

# ---------------- FOOTBALL LINKS ----------------

st.markdown('<div class="section-title">{T["explore"]}</div>', unsafe_allow_html=True)

a, b, c, d = st.columns(4)

with a:
    st.link_button("📰 Noticias FIFA", FIFA_LINKS["Noticias"], use_container_width=True)

with b:
    st.link_button("🏆 Torneos FIFA", FIFA_LINKS["Torneos"], use_container_width=True)

with c:
    st.link_button("📊 Centro de partidos FIFA", FIFA_LINKS["Partidos y estadísticas"], use_container_width=True)

with d:
    st.link_button("🎮 FIFA Play", FIFA_LINKS["Jugar"], use_container_width=True)

# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="hero">
        <h2 style="color:white;">🌎 EL FÚTBOL UNE AL MUNDO</h2>
        <p style="color:#d9eaff;font-size:18px;">
            Explora la historia, los jugadores, los torneos y los momentos
            que han convertido al fútbol en el deporte del mundo.
        </p>
    </div>

    <div class="disclaimer">
        FIFA Football Legends es un proyecto no oficial creado por fans.
        No está afiliado, respaldado ni operado por FIFA.
    </div>

    <div class="footer">
        <h3>⚽ FIFA FOOTBALL LEGENDS</h3>
        Celebrando a los mejores jugadores, historias y momentos del fútbol.
    </div>
    """,
    unsafe_allow_html=True
)