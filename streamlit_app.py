import os
import sqlite3
import uuid
from datetime import datetime
from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="TechScaler Solutions - Admission Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# APP CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE = BASE_DIR / "database.db"

UPLOAD_FOLDER = BASE_DIR / "uploads" / "payments"

STATIC_FOLDER = BASE_DIR / "static"

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
STATIC_FOLDER.mkdir(parents=True, exist_ok=True)


LOGO_PATH = STATIC_FOLDER / "logo.png"
QR_PATH = STATIC_FOLDER / "qr.png"


# ============================================================
# ADMIN LOGIN
# ============================================================

# For Streamlit Cloud you can later move these to Secrets.
ADMIN_USERNAME = os.environ.get(
    "ADMIN_USERNAME",
    "admin"
)

ADMIN_PASSWORD = os.environ.get(
    "ADMIN_PASSWORD",
    "admin123"
)


# ============================================================
# INSTITUTE DETAILS
# ============================================================

INSTITUTE_NAME = "TechScaler Solutions"

TAGLINE = (
    "Data Science | Data Analytics | Python | Power BI | "
    "SQL | Machine Learning | GenAI"
)

PHONE = "082377 11856"

EMAIL = "info@techscalersolutions.com"

ADDRESS = (
    "2nd Floor, Tandale Prestige, Senapati Bapat Rd, "
    "Above Mulchand Sweets, Range Hill Corner, "
    "Jawahar Nagar, Shivajinagar, Pune, Maharashtra 411016"
)

WEBSITE = "https://techscalersolutions.com"


# ============================================================
# COURSES
# ============================================================

COURSES = [
    "Data Science",
    "Data Analytics",
    "Python",
    "Power BI",
    "SQL",
    "Machine Learning",
    "GenAI",
    "R Programming",
    "Clinical SAS",
    "Base SAS",
    "NLP",
    "Artificial Intelligence"
]


# ============================================================
# UPLOAD SETTINGS
# ============================================================

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "webp",
    "pdf"
}

MAX_FILE_SIZE = 10 * 1024 * 1024


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

    /* =====================================================
       GLOBAL
    ===================================================== */

    .stApp {
        background: #f4f7fb;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* =====================================================
       HEADER
    ===================================================== */

    .top-header {
        background: linear-gradient(
            135deg,
            #ff6a00,
            #ff8c00
        );

        color: white;

        padding: 20px 28px;

        border-radius: 16px;

        box-shadow:
            0 5px 18px rgba(0,0,0,0.12);

        margin-bottom: 25px;
    }


    .brand-title {
        font-size: 30px;
        font-weight: 900;
        margin-bottom: 5px;
    }


    .brand-tagline {
        font-size: 14px;
        opacity: 0.95;
    }


    /* =====================================================
       HERO
    ===================================================== */

    .hero {
        background:
            linear-gradient(
                90deg,
                rgba(17,24,39,0.94),
                rgba(17,24,39,0.70)
            ),
            url(
                "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1800&q=85"
            );

        background-size: cover;
        background-position: center;

        min-height: 330px;

        border-radius: 20px;

        padding: 50px;

        display: flex;
        align-items: center;

        color: white;

        margin-bottom: 30px;
    }


    .hero h1 {
        font-size: 44px;
        font-weight: 900;
        margin-bottom: 12px;
    }


    .hero p {
        font-size: 17px;
        line-height: 1.7;
        max-width: 750px;
    }


    .hero-badge {
        display: inline-block;

        background: #ff6a00;

        padding: 8px 15px;

        border-radius: 30px;

        font-size: 13px;

        font-weight: 800;

        margin-bottom: 15px;
    }


    /* =====================================================
       CARDS
    ===================================================== */

    .card {
        background: white;

        border-radius: 15px;

        padding: 25px;

        margin-bottom: 20px;

        border: 1px solid #e5e7eb;

        box-shadow:
            0 4px 18px rgba(0,0,0,0.06);
    }


    .card-title {
        color: #ff6a00;

        font-size: 25px;

        font-weight: 900;

        margin-bottom: 10px;
    }


    /* =====================================================
       COURSE CARDS
    ===================================================== */

    .course-card {
        background: white;

        border-radius: 15px;

        padding: 22px;

        min-height: 145px;

        border: 1px solid #e5e7eb;

        box-shadow:
            0 4px 15px rgba(0,0,0,0.05);

        margin-bottom: 18px;
    }


    .course-icon {
        font-size: 30px;
    }


    .course-name {
        font-size: 18px;

        font-weight: 800;

        margin-top: 8px;
    }


    /* =====================================================
       PAYMENT BOX
    ===================================================== */

    .payment-box {
        background: #fff7ed;

        border: 2px solid #fed7aa;

        border-radius: 14px;

        padding: 22px;

        margin-top: 20px;
        margin-bottom: 20px;
    }


    .payment-title {
        color: #c2410c;

        font-size: 23px;

        font-weight: 900;
    }


    /* =====================================================
       ADMIN STATS
    ===================================================== */

    .stat-card {
        background: white;

        padding: 20px;

        border-radius: 14px;

        border: 1px solid #e5e7eb;

        box-shadow:
            0 4px 15px rgba(0,0,0,0.05);

        text-align: center;
    }


    .stat-number {
        color: #ff6a00;

        font-size: 28px;

        font-weight: 900;
    }


    .stat-label {
        color: #6b7280;

        font-size: 14px;

        margin-top: 5px;
    }


    /* =====================================================
       STATUS
    ===================================================== */

    .status {
        display: inline-block;

        padding: 6px 13px;

        border-radius: 25px;

        font-weight: 800;

        font-size: 13px;
    }


    .status-pending {
        background: #fef3c7;
        color: #92400e;
    }


    .status-verified {
        background: #dcfce7;
        color: #166534;
    }


    .status-rejected {
        background: #fee2e2;
        color: #991b1b;
    }


    /* =====================================================
       RECEIPT
    ===================================================== */

    .receipt {
        position: relative;

        background: white;

        max-width: 900px;

        margin: 20px auto;

        padding: 40px;

        border: 1px solid #ddd;

        border-radius: 10px;

        box-shadow:
            0 5px 25px rgba(0,0,0,0.08);
    }


    .receipt-header {
        text-align: center;

        border-bottom: 2px solid #ff6a00;

        padding-bottom: 20px;

        margin-bottom: 25px;
    }


    .receipt-header h1 {
        color: #ff6a00;

        font-size: 30px;

        margin-bottom: 5px;
    }


    .receipt-row {
        display: flex;

        justify-content: space-between;

        gap: 20px;

        padding: 10px 0;

        border-bottom: 1px solid #eeeeee;
    }


    .receipt-label {
        font-weight: 800;
    }


    .receipt-value {
        text-align: right;
    }


    /* =====================================================
       PAID / VERIFIED STAMP
    ===================================================== */

    .paid-stamp {

        position: absolute;

        right: 55px;

        top: 185px;

        width: 145px;

        height: 145px;

        border: 6px solid #16a34a;

        border-radius: 50%;

        display: flex;

        align-items: center;

        justify-content: center;

        transform: rotate(-14deg);

        opacity: 0.88;

        color: #16a34a;

        font-weight: 900;

        text-align: center;

        font-size: 21px;

        line-height: 1.15;

        background: rgba(
            240,
            253,
            244,
            0.55
        );

        box-shadow:
            inset 0 0 0 3px
            rgba(22,163,74,0.15);

        pointer-events: none;
    }


    .paid-stamp::before {

        content: "";

        position: absolute;

        inset: 8px;

        border: 2px dashed #16a34a;

        border-radius: 50%;
    }


    .paid-stamp small {

        display: block;

        font-size: 8px;

        margin-top: 5px;

        letter-spacing: 1px;
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer {

        background: #111827;

        color: white;

        padding: 30px;

        border-radius: 15px;

        margin-top: 40px;

        text-align: center;
    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media(max-width:700px) {

        .hero {
            padding: 25px;
            min-height: 270px;
        }

        .hero h1 {
            font-size: 30px;
        }

        .brand-title {
            font-size: 24px;
        }

        .receipt {
            padding: 20px;
        }

        .paid-stamp {
            position: relative;
            right: auto;
            top: auto;
            margin: 20px auto;
        }

        .receipt-row {
            flex-direction: column;
            gap: 4px;
        }

        .receipt-value {
            text-align: left;
        }
    }

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def get_db():

    conn = sqlite3.connect(
        str(DATABASE),
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row

    return conn


def initialize_database():

    conn = get_db()

    cursor = conn.cursor()


    # --------------------------------------------------------
    # STUDENTS TABLE
    # --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            admission_id TEXT UNIQUE NOT NULL,

            name TEXT NOT NULL,

            email TEXT,

            phone TEXT NOT NULL,

            course TEXT NOT NULL,

            batch TEXT,

            mode TEXT,

            address TEXT,

            created_at TEXT NOT NULL

        )
        """
    )


    # --------------------------------------------------------
    # MIGRATION
    # --------------------------------------------------------

    cursor.execute(
        "PRAGMA table_info(students)"
    )

    student_columns = [
        column["name"]
        for column in cursor.fetchall()
    ]


    if "batch" not in student_columns:

        cursor.execute(
            """
            ALTER TABLE students
            ADD COLUMN batch TEXT
            """
        )


    if "mode" not in student_columns:

        cursor.execute(
            """
            ALTER TABLE students
            ADD COLUMN mode TEXT
            """
        )


    # --------------------------------------------------------
    # PAYMENTS TABLE
    # --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS payments (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            admission_id TEXT NOT NULL,

            installment_amount REAL NOT NULL,

            payment_screenshot TEXT,

            payment_status TEXT DEFAULT 'Pending',

            payment_date TEXT NOT NULL,

            FOREIGN KEY(admission_id)
            REFERENCES students(admission_id)

        )
        """
    )


    conn.commit()

    conn.close()


initialize_database()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def allowed_file(filename):

    if not filename:

        return False

    if "." not in filename:

        return False

    extension = (
        filename
        .rsplit(".", 1)[1]
        .lower()
    )

    return extension in ALLOWED_EXTENSIONS


def generate_admission_id():

    while True:

        date_part = datetime.now().strftime(
            "%Y%m%d"
        )

        random_part = uuid.uuid4().hex[:6].upper()

        admission_id = (
            f"TS-{date_part}-{random_part}"
        )

        conn = get_db()

        existing = conn.execute(
            """
            SELECT id
            FROM students
            WHERE admission_id = ?
            """,
            (admission_id,)
        ).fetchone()

        conn.close()

        if not existing:

            return admission_id


def save_payment_file(
    uploaded_file,
    admission_id
):

    if uploaded_file is None:

        return None


    if not allowed_file(
        uploaded_file.name
    ):

        return None


    file_size = uploaded_file.size

    if file_size > MAX_FILE_SIZE:

        return None


    original_name = Path(
        uploaded_file.name
    ).name


    extension = ""

    if "." in original_name:

        extension = (
            original_name
            .rsplit(".", 1)[1]
            .lower()
        )


    filename = (
        f"{admission_id}-PAYMENT-1."
        f"{extension}"
    )


    file_path = (
        UPLOAD_FOLDER / filename
    )


    with open(
        file_path,
        "wb"
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )


    return filename


def get_student(admission_id):

    conn = get_db()

    student = conn.execute(
        """
        SELECT *
        FROM students
        WHERE admission_id = ?
        """,
        (admission_id,)
    ).fetchone()

    conn.close()

    return student


def get_payments(admission_id):

    conn = get_db()

    payments = conn.execute(
        """
        SELECT *
        FROM payments
        WHERE admission_id = ?
        ORDER BY id ASC
        """,
        (admission_id,)
    ).fetchall()

    conn.close()

    return payments


def get_status_html(status):

    if status == "Verified":

        return (
            '<span class="status status-verified">'
            '✓ VERIFIED'
            '</span>'
        )

    if status == "Rejected":

        return (
            '<span class="status status-rejected">'
            '✕ REJECTED'
            '</span>'
        )

    return (
        '<span class="status status-pending">'
        '⏳ PENDING'
        '</span>'
    )


def calculate_totals(admission_id):

    conn = get_db()

    verified = conn.execute(
        """
        SELECT COALESCE(
            SUM(installment_amount),
            0
        )

        FROM payments

        WHERE admission_id = ?

        AND payment_status = 'Verified'
        """,
        (admission_id,)
    ).fetchone()[0]


    pending = conn.execute(
        """
        SELECT COALESCE(
            SUM(installment_amount),
            0
        )

        FROM payments

        WHERE admission_id = ?

        AND payment_status = 'Pending'
        """,
        (admission_id,)
    ).fetchone()[0]


    rejected = conn.execute(
        """
        SELECT COALESCE(
            SUM(installment_amount),
            0
        )

        FROM payments

        WHERE admission_id = ?

        AND payment_status = 'Rejected'
        """,
        (admission_id,)
    ).fetchone()[0]


    conn.close()


    return (
        verified or 0,
        pending or 0,
        rejected or 0
    )


# ============================================================
# SESSION STATE
# ============================================================

if "admin_logged_in" not in st.session_state:

    st.session_state.admin_logged_in = False


if "page" not in st.session_state:

    st.session_state.page = "Home"


if "receipt_id" not in st.session_state:

    st.session_state.receipt_id = None


if "check_admission_id" not in st.session_state:

    st.session_state.check_admission_id = ""


# ============================================================
# HEADER
# ============================================================

logo_exists = LOGO_PATH.exists()

header_col1, header_col2 = st.columns(
    [1, 7]
)


with header_col1:

    if logo_exists:

        st.image(
            str(LOGO_PATH),
            width=80
        )

    else:

        st.markdown(
            """
            <div style="
                background:white;
                color:#ff6a00;
                width:75px;
                height:75px;
                border-radius:12px;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:25px;
                font-weight:bold;
            ">
                TS
            </div>
            """,
            unsafe_allow_html=True
        )


with header_col2:

    st.markdown(
        f"""
        <div class="top-header">

            <div class="brand-title">
                {INSTITUTE_NAME}
            </div>

            <div class="brand-tagline">
                {TAGLINE}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🎓 TechScaler"
    )

    st.markdown("---")


    navigation = [
        "🏠 Home",
        "📝 Admission Form",
        "🔎 Check Admission",
        "🔐 Admin"
    ]


    selected_navigation = st.radio(
        "Navigation",
        navigation
    )


    st.markdown("---")


    st.markdown(
        "### 📞 Contact"
    )

    st.write(PHONE)

    st.write(EMAIL)

    st.markdown("---")

    st.caption(
        "© TechScaler Solutions"
    )


# ============================================================
# HOME
# ============================================================

if selected_navigation == "🏠 Home":

    st.markdown(
        """
        <div class="hero">

            <div>

                <div class="hero-badge">
                    🎓 CAREER-FOCUSED TRAINING
                </div>

                <h1>
                    Build Your Career With TechScaler
                </h1>

                <p>
                    Learn industry-ready skills in Data Science,
                    Data Analytics, Python, Power BI, SQL,
                    Machine Learning and Generative AI.
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        "## 🚀 Our Courses"
    )


    course_icons = {

        "Data Science": "📊",

        "Data Analytics": "📈",

        "Python": "🐍",

        "Power BI": "📉",

        "SQL": "🗄️",

        "Machine Learning": "🤖",

        "GenAI": "🧠",

        "R Programming": "📐",

        "Clinical SAS": "🧬",

        "Base SAS": "💻",

        "NLP": "💬",

        "Artificial Intelligence": "🚀"
    }


    course_columns = st.columns(4)


    for index, course in enumerate(COURSES):

        with course_columns[index % 4]:

            st.markdown(
                f"""
                <div class="course-card">

                    <div class="course-icon">
                        {course_icons.get(
                            course,
                            "🎓"
                        )}
                    </div>

                    <div class="course-name">
                        {course}
                    </div>

                    <p style="
                        color:#6b7280;
                        font-size:13px;
                    ">
                        Industry-focused learning
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    st.markdown(
        "## ⭐ Why TechScaler?"
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    🎯 Practical Learning
                </div>

                <p>
                    Learn through practical projects,
                    assignments and real-world examples.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    💼 Career Support
                </div>

                <p>
                    Resume guidance, interview preparation
                    and placement assistance.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    👨‍💻 Industry Skills
                </div>

                <p>
                    Learn tools and technologies used
                    by modern data and AI teams.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        f"""
        <div class="footer">

            <h3>
                {INSTITUTE_NAME}
            </h3>

            <p>
                {TAGLINE}
            </p>

            <p>
                📞 {PHONE}
                &nbsp; | &nbsp;
                ✉️ {EMAIL}
            </p>

            <p>
                {ADDRESS}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ADMISSION FORM
# ============================================================

elif selected_navigation == "📝 Admission Form":

    st.markdown(
        "## 📝 Student Admission Form"
    )


    st.info(
        "Please fill in your details and submit your first installment payment."
    )


    with st.form(
        "student_admission_form"
    ):

        st.markdown(
            "### 👤 Student Information"
        )


        c1, c2 = st.columns(2)


        with c1:

            name = st.text_input(
                "Student Name *",
                placeholder="Enter student name"
            )


            phone = st.text_input(
                "Mobile Number *",
                placeholder="Enter mobile number"
            )


        with c2:

            email = st.text_input(
                "Email",
                placeholder="Enter email address"
            )


            course = st.selectbox(
                "Course *",
                [
                    "Select Course"
                ] + COURSES
            )


        c3, c4 = st.columns(2)


        with c3:

            batch = st.text_input(
                "Batch",
                placeholder=(
                    "Example: Weekend / Weekday / 8 PM"
                )
            )


        with c4:

            mode = st.selectbox(
                "Mode",
                [
                    "Select Mode",
                    "Online",
                    "Offline",
                    "Hybrid"
                ]
            )


        address = st.text_area(
            "Address",
            placeholder="Enter complete address"
        )


        st.markdown(
            """
            <div class="payment-box">

                <div class="payment-title">
                    💳 Payment Details
                </div>

                <p>
                    You can pay any installment amount such as
                    ₹5,000, ₹10,000, ₹15,000, etc.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        qr_col1, qr_col2 = st.columns(
            [1, 2]
        )


        with qr_col1:

            if QR_PATH.exists():

                st.image(
                    str(QR_PATH),
                    caption="Scan QR to make payment",
                    width=230
                )

            else:

                st.warning(
                    "QR code not found. "
                    "Place your payment QR as static/qr.png"
                )


        with qr_col2:

            st.markdown(
                """
                ### 📱 Payment Steps

                1. Scan the QR code.
                2. Pay your installment amount.
                3. Take a screenshot of successful payment.
                4. Upload the screenshot.
                5. Submit the admission form.

                **Payment will initially be marked Pending.**
                """
            )


        installment_amount = st.number_input(
            "Installment Amount (₹) *",
            min_value=1.0,
            value=5000.0,
            step=500.0
        )


        payment_screenshot = st.file_uploader(
            "Payment Screenshot *",
            type=[
                "png",
                "jpg",
                "jpeg",
                "webp",
                "pdf"
            ]
        )


        submitted = st.form_submit_button(
            "🚀 Submit Admission",
            use_container_width=True
        )


    if submitted:

        errors = []


        if not name.strip():

            errors.append(
                "Student name is required."
            )


        if not phone.strip():

            errors.append(
                "Mobile number is required."
            )


        if course == "Select Course":

            errors.append(
                "Please select a valid course."
            )


        if installment_amount <= 0:

            errors.append(
                "Installment amount must be greater than zero."
            )


        if payment_screenshot is None:

            errors.append(
                "Payment screenshot is required."
            )


        if payment_screenshot:

            if not allowed_file(
                payment_screenshot.name
            ):

                errors.append(
                    "Invalid payment file. "
                    "Use JPG, JPEG, PNG, WEBP or PDF."
                )


            elif payment_screenshot.size > MAX_FILE_SIZE:

                errors.append(
                    "Payment screenshot must be smaller than 10 MB."
                )


        if errors:

            for error in errors:

                st.error(error)


        else:

            admission_id = generate_admission_id()


            filename = save_payment_file(
                payment_screenshot,
                admission_id
            )


            if not filename:

                st.error(
                    "Unable to save payment screenshot."
                )

            else:

                created_at = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )


                conn = get_db()


                try:

                    # ----------------------------------------
                    # INSERT STUDENT
                    # ----------------------------------------

                    conn.execute(
                        """
                        INSERT INTO students
                        (
                            admission_id,
                            name,
                            email,
                            phone,
                            course,
                            batch,
                            mode,
                            address,
                            created_at
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            admission_id,
                            name.strip(),
                            email.strip(),
                            phone.strip(),
                            course,
                            batch.strip(),
                            (
                                ""
                                if mode == "Select Mode"
                                else mode
                            ),
                            address.strip(),
                            created_at
                        )
                    )


                    # ----------------------------------------
                    # INSERT PAYMENT
                    # ----------------------------------------

                    conn.execute(
                        """
                        INSERT INTO payments
                        (
                            admission_id,
                            installment_amount,
                            payment_screenshot,
                            payment_status,
                            payment_date
                        )
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            admission_id,
                            float(installment_amount),
                            filename,
                            "Pending",
                            created_at
                        )
                    )


                    conn.commit()


                    st.success(
                        "🎉 Admission submitted successfully!"
                    )


                    st.markdown(
                        f"""
                        <div class="card">

                            <h2>
                                Admission Submitted Successfully
                            </h2>

                            <p>
                                Thank you for registering with
                                <strong>
                                    TechScaler Solutions
                                </strong>.
                            </p>

                            <div class="payment-box">

                                <h3>
                                    Admission ID
                                </h3>

                                <h2>
                                    {admission_id}
                                </h2>

                                <p>
                                    <strong>
                                        Student:
                                    </strong>
                                    {name}
                                </p>

                                <p>
                                    <strong>
                                        Course:
                                    </strong>
                                    {course}
                                </p>

                                <p>
                                    <strong>
                                        Installment:
                                    </strong>
                                    ₹{installment_amount:,.2f}
                                </p>

                                <p>
                                    <strong>
                                        Payment Status:
                                    </strong>
                                    Pending Verification
                                </p>

                            </div>

                            <p>
                                Please save your Admission ID
                                for future reference.
                            </p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                except sqlite3.IntegrityError as error:

                    conn.rollback()

                    file_path = (
                        UPLOAD_FOLDER / filename
                    )

                    if file_path.exists():

                        file_path.unlink()


                    st.error(
                        f"Database error: {error}"
                    )


                except Exception as error:

                    conn.rollback()

                    file_path = (
                        UPLOAD_FOLDER / filename
                    )

                    if file_path.exists():

                        file_path.unlink()


                    st.error(
                        f"Something went wrong: {error}"
                    )


                finally:

                    conn.close()


# ============================================================
# CHECK ADMISSION
# ============================================================

elif selected_navigation == "🔎 Check Admission":

    st.markdown(
        "## 🔎 Check Admission"
    )


    admission_id = st.text_input(
        "Enter Admission ID",
        value=st.session_state.check_admission_id,
        placeholder="Example: TS-20261004-ABC123"
    )


    if st.button(
        "🔍 Search Admission",
        use_container_width=True
    ):

        admission_id = (
            admission_id.strip().upper()
        )


        st.session_state.check_admission_id = (
            admission_id
        )


        student = get_student(
            admission_id
        )


        if not student:

            st.error(
                "Admission ID not found."
            )

        else:

            st.success(
                "Admission record found."
            )


            st.markdown(
                f"""
                <div class="card">

                    <div class="card-title">
                        Student Details
                    </div>

                    <div class="receipt-row">

                        <span class="receipt-label">
                            Admission ID
                        </span>

                        <span class="receipt-value">
                            {student["admission_id"]}
                        </span>

                    </div>

                    <div class="receipt-row">

                        <span class="receipt-label">
                            Student Name
                        </span>

                        <span class="receipt-value">
                            {student["name"]}
                        </span>

                    </div>

                    <div class="receipt-row">

                        <span class="receipt-label">
                            Course
                        </span>

                        <span class="receipt-value">
                            {student["course"]}
                        </span>

                    </div>

                    <div class="receipt-row">

                        <span class="receipt-label">
                            Batch
                        </span>

                        <span class="receipt-value">
                            {student["batch"] or "-"}
                        </span>

                    </div>

                    <div class="receipt-row">

                        <span class="receipt-label">
                            Mode
                        </span>

                        <span class="receipt-value">
                            {student["mode"] or "-"}
                        </span>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            payments = get_payments(
                admission_id
            )


            st.markdown(
                "### 💳 Payment History"
            )


            if payments:

                verified_total = 0


                for payment in payments:

                    amount = float(
                        payment["installment_amount"]
                    )

                    status = payment[
                        "payment_status"
                    ]


                    if status == "Verified":

                        verified_total += amount


                    with st.container(
                        border=True
                    ):

                        p1, p2, p3 = st.columns(3)


                        with p1:

                            st.write(
                                "**Installment**"
                            )

                            st.write(
                                f"₹{amount:,.2f}"
                            )


                        with p2:

                            st.write(
                                "**Date**"
                            )

                            st.write(
                                payment["payment_date"]
                            )


                        with p3:

                            st.write(
                                "**Status**"
                            )

                            st.markdown(
                                get_status_html(
                                    status
                                ),
                                unsafe_allow_html=True
                            )


                st.metric(
                    "Total Verified Amount",
                    f"₹{verified_total:,.2f}"
                )


                if st.button(
                    "🧾 View Receipt",
                    use_container_width=True
                ):

                    st.session_state.receipt_id = (
                        admission_id
                    )

                    st.rerun()


            else:

                st.info(
                    "No payment records found."
                )


# ============================================================
# ADMIN
# ============================================================

elif selected_navigation == "🔐 Admin":

    # ========================================================
    # LOGIN
    # ========================================================

    if not st.session_state.admin_logged_in:

        st.markdown(
            "## 🔐 Admin Login"
        )


        with st.form(
            "admin_login"
        ):

            username = st.text_input(
                "Username"
            )

            password = st.text_input(
                "Password",
                type="password"
            )


            login = st.form_submit_button(
                "🔐 Login",
                use_container_width=True
            )


        if login:

            if (
                username == ADMIN_USERNAME
                and
                password == ADMIN_PASSWORD
            ):

                st.session_state.admin_logged_in = True

                st.success(
                    "Login successful."
                )

                st.rerun()

            else:

                st.error(
                    "Invalid admin username or password."
                )


    # ========================================================
    # ADMIN DASHBOARD
    # ========================================================

    else:

        st.markdown(
            "## 📊 Admin Dashboard"
        )


        if st.button(
            "🚪 Logout"
        ):

            st.session_state.admin_logged_in = False

            st.rerun()


        # ----------------------------------------------------
        # STATISTICS
        # ----------------------------------------------------

        conn = get_db()


        total_students = conn.execute(
            """
            SELECT COUNT(*)
            FROM students
            """
        ).fetchone()[0]


        total_payments = conn.execute(
            """
            SELECT COUNT(*)
            FROM payments
            """
        ).fetchone()[0]


        pending_payments = conn.execute(
            """
            SELECT COUNT(*)
            FROM payments
            WHERE payment_status = 'Pending'
            """
        ).fetchone()[0]


        verified_amount = conn.execute(
            """
            SELECT COALESCE(
                SUM(installment_amount),
                0
            )

            FROM payments

            WHERE payment_status = 'Verified'
            """
        ).fetchone()[0]


        conn.close()


        stat1, stat2, stat3, stat4 = st.columns(4)


        with stat1:

            st.markdown(
                f"""
                <div class="stat-card">

                    <div class="stat-number">
                        {total_students}
                    </div>

                    <div class="stat-label">
                        Total Students
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        with stat2:

            st.markdown(
                f"""
                <div class="stat-card">

                    <div class="stat-number">
                        {total_payments}
                    </div>

                    <div class="stat-label">
                        Total Payments
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        with stat3:

            st.markdown(
                f"""
                <div class="stat-card">

                    <div class="stat-number">
                        {pending_payments}
                    </div>

                    <div class="stat-label">
                        Pending Payments
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        with stat4:

            st.markdown(
                f"""
                <div class="stat-card">

                    <div class="stat-number">
                        ₹{verified_amount:,.0f}
                    </div>

                    <div class="stat-label">
                        Verified Amount
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        st.markdown("---")


        # ----------------------------------------------------
        # SEARCH
        # ----------------------------------------------------

        st.markdown(
            "### 🔎 Search & Filter"
        )


        c1, c2 = st.columns(2)


        with c1:

            search = st.text_input(
                "Search Student",
                placeholder=(
                    "Admission ID / Name / Phone / Email"
                )
            )


        with c2:

            status_filter = st.selectbox(
                "Payment Status",
                [
                    "All",
                    "Pending",
                    "Verified",
                    "Rejected"
                ]
            )


        # ----------------------------------------------------
        # LOAD STUDENTS
        # ----------------------------------------------------

        conn = get_db()


        query = """
            SELECT *
            FROM students
            WHERE 1=1
        """


        params = []


        if search.strip():

            query += """
                AND (
                    admission_id LIKE ?
                    OR name LIKE ?
                    OR phone LIKE ?
                    OR email LIKE ?
                )
            """


            search_value = (
                f"%{search.strip()}%"
            )


            params.extend(
                [
                    search_value,
                    search_value,
                    search_value,
                    search_value
                ]
            )


        query += """
            ORDER BY id DESC
        """


        students = conn.execute(
            query,
            params
        ).fetchall()


        conn.close()


        # ----------------------------------------------------
        # STUDENT RECORDS
        # ----------------------------------------------------

        displayed_students = 0


        for student in students:

            payments = get_payments(
                student["admission_id"]
            )


            # -----------------------------------------------
            # STATUS FILTER
            # -----------------------------------------------

            statuses = [
                payment["payment_status"]
                for payment in payments
            ]


            if status_filter != "All":

                if status_filter not in statuses:

                    continue


            displayed_students += 1


            verified_total, pending_total, rejected_total = (
                calculate_totals(
                    student["admission_id"]
                )
            )


            with st.expander(
                f"🎓 {student['name']} "
                f"— {student['admission_id']}"
            ):


                # -------------------------------------------
                # STUDENT INFORMATION
                # -------------------------------------------

                st.markdown(
                    "### 👤 Student Information"
                )


                c1, c2 = st.columns(2)


                with c1:

                    st.write(
                        f"**Name:** {student['name']}"
                    )

                    st.write(
                        f"**Phone:** {student['phone']}"
                    )

                    st.write(
                        f"**Email:** "
                        f"{student['email'] or '-'}"
                    )

                    st.write(
                        f"**Course:** "
                        f"{student['course']}"
                    )


                with c2:

                    st.write(
                        f"**Batch:** "
                        f"{student['batch'] or '-'}"
                    )

                    st.write(
                        f"**Mode:** "
                        f"{student['mode'] or '-'}"
                    )

                    st.write(
                        f"**Admission ID:** "
                        f"{student['admission_id']}"
                    )

                    st.write(
                        f"**Created:** "
                        f"{student['created_at']}"
                    )


                st.markdown("---")


                # -------------------------------------------
                # PAYMENT TOTALS
                # -------------------------------------------

                st.markdown(
                    "### 💰 Payment Summary"
                )


                t1, t2, t3 = st.columns(3)


                with t1:

                    st.metric(
                        "Verified",
                        f"₹{verified_total:,.2f}"
                    )


                with t2:

                    st.metric(
                        "Pending",
                        f"₹{pending_total:,.2f}"
                    )


                with t3:

                    st.metric(
                        "Rejected",
                        f"₹{rejected_total:,.2f}"
                    )


                # -------------------------------------------
                # PAYMENT HISTORY
                # -------------------------------------------

                st.markdown(
                    "### 💳 Payment Records"
                )


                if not payments:

                    st.info(
                        "No payment records."
                    )


                for payment in payments:

                    payment_id = payment["id"]

                    amount = float(
                        payment[
                            "installment_amount"
                        ]
                    )

                    payment_status = payment[
                        "payment_status"
                    ]

                    screenshot = payment[
                        "payment_screenshot"
                    ]


                    st.markdown(
                        f"""
                        <div class="card">

                            <strong>
                                Payment #{payment_id}
                            </strong>

                            <br><br>

                            Amount:
                            <strong>
                                ₹{amount:,.2f}
                            </strong>

                            <br>

                            Date:
                            {payment["payment_date"]}

                            <br><br>

                            {get_status_html(
                                payment_status
                            )}

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    # ---------------------------------------
                    # SCREENSHOT
                    # ---------------------------------------

                    if screenshot:

                        file_path = (
                            UPLOAD_FOLDER
                            / screenshot
                        )


                        if file_path.exists():

                            if file_path.suffix.lower() == ".pdf":

                                with open(
                                    file_path,
                                    "rb"
                                ) as pdf_file:

                                    st.download_button(
                                        "⬇️ Download Payment PDF",
                                        data=pdf_file.read(),
                                        file_name=file_path.name,
                                        key=(
                                            f"pdf_"
                                            f"{payment_id}"
                                        )
                                    )

                            else:

                                st.image(
                                    str(file_path),
                                    caption=(
                                        "Payment Screenshot"
                                    ),
                                    width=450
                                )


                                with open(
                                    file_path,
                                    "rb"
                                ) as image_file:

                                    st.download_button(
                                        "⬇️ Download Screenshot",
                                        data=image_file.read(),
                                        file_name=file_path.name,
                                        key=(
                                            f"img_"
                                            f"{payment_id}"
                                        )
                                    )


                    # ---------------------------------------
                    # ACTIONS
                    # ---------------------------------------

                    a1, a2, a3 = st.columns(3)


                    with a1:

                        if st.button(
                            "✓ Verify",
                            key=(
                                f"verify_"
                                f"{payment_id}"
                            ),
                            use_container_width=True
                        ):

                            conn = get_db()

                            conn.execute(
                                """
                                UPDATE payments

                                SET payment_status = 'Verified'

                                WHERE id = ?
                                """,
                                (payment_id,)
                            )

                            conn.commit()

                            conn.close()

                            st.success(
                                "Payment verified."
                            )

                            st.rerun()


                    with a2:

                        if st.button(
                            "✕ Reject",
                            key=(
                                f"reject_"
                                f"{payment_id}"
                            ),
                            use_container_width=True
                        ):

                            conn = get_db()

                            conn.execute(
                                """
                                UPDATE payments

                                SET payment_status = 'Rejected'

                                WHERE id = ?
                                """,
                                (payment_id,)
                            )

                            conn.commit()

                            conn.close()

                            st.warning(
                                "Payment rejected."
                            )

                            st.rerun()


                    with a3:

                        if st.button(
                            "⏳ Pending",
                            key=(
                                f"pending_"
                                f"{payment_id}"
                            ),
                            use_container_width=True
                        ):

                            conn = get_db()

                            conn.execute(
                                """
                                UPDATE payments

                                SET payment_status = 'Pending'

                                WHERE id = ?
                                """,
                                (payment_id,)
                            )

                            conn.commit()

                            conn.close()

                            st.info(
                                "Payment moved to Pending."
                            )

                            st.rerun()


                # -------------------------------------------
                # PAYMENT HISTORY / RECEIPT
                # -------------------------------------------

                st.markdown("---")


                h1, h2 = st.columns(2)


                with h1:

                    if st.button(
                        "📜 Payment History",
                        key=(
                            f"history_"
                            f"{student['admission_id']}"
                        ),
                        use_container_width=True
                    ):

                        st.session_state.history_id = (
                            student["admission_id"]
                        )

                        st.rerun()


                with h2:

                    if st.button(
                        "🧾 View Receipt",
                        key=(
                            f"receipt_"
                            f"{student['admission_id']}"
                        ),
                        use_container_width=True
                    ):

                        st.session_state.receipt_id = (
                            student["admission_id"]
                        )

                        st.rerun()


        if displayed_students == 0:

            st.info(
                "No students found for the selected filter."
            )


# ============================================================
# PAYMENT HISTORY PAGE
# ============================================================

if (
    st.session_state.get("history_id")
    and st.session_state.admin_logged_in
):

    history_id = (
        st.session_state.history_id
    )


    st.markdown("---")

    st.markdown(
        "## 📜 Payment History"
    )


    student = get_student(
        history_id
    )


    if student:

        payments = get_payments(
            history_id
        )


        verified_total, pending_total, rejected_total = (
            calculate_totals(
                history_id
            )
        )


        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    {student["name"]}
                </div>

                <p>
                    <strong>
                        Admission ID:
                    </strong>
                    {student["admission_id"]}
                </p>

                <p>
                    <strong>
                        Course:
                    </strong>
                    {student["course"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "Verified",
                f"₹{verified_total:,.2f}"
            )


        with c2:

            st.metric(
                "Pending",
                f"₹{pending_total:,.2f}"
            )


        with c3:

            st.metric(
                "Rejected",
                f"₹{rejected_total:,.2f}"
            )


        for index, payment in enumerate(
            payments,
            start=1
        ):

            st.markdown(
                f"""
                <div class="card">

                    <h4>
                        Installment #{index}
                    </h4>

                    <p>
                        <strong>
                            Amount:
                        </strong>
                        ₹{float(
                            payment["installment_amount"]
                        ):,.2f}
                    </p>

                    <p>
                        <strong>
                            Date:
                        </strong>
                        {payment["payment_date"]}
                    </p>

                    <p>
                        {get_status_html(
                            payment["payment_status"]
                        )}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


        if st.button(
            "❌ Close Payment History",
            use_container_width=True
        ):

            st.session_state.history_id = None

            st.rerun()


# ============================================================
# RECEIPT
# ============================================================

if st.session_state.get("receipt_id"):

    receipt_id = (
        st.session_state.receipt_id
    )


    student = get_student(
        receipt_id
    )


    if student:

        payments = get_payments(
            receipt_id
        )


        verified_total, pending_total, rejected_total = (
            calculate_totals(
                receipt_id
            )
        )


        has_verified_payment = any(
            payment["payment_status"]
            == "Verified"

            for payment in payments
        )


        st.markdown("---")


        st.markdown(
            "## 🧾 Admission Receipt"
        )


        # ----------------------------------------------------
        # RECEIPT HEADER
        # ----------------------------------------------------

        stamp_html = ""


        if has_verified_payment:

            stamp_html = """
            <div class="paid-stamp">

                <div>

                    PAID

                    <div style="
                        font-size:14px;
                    ">
                        VERIFIED
                    </div>

                    <small>
                        TECHSCALER SOLUTIONS
                    </small>

                </div>

            </div>
            """


        payment_rows = ""


        for index, payment in enumerate(
            payments,
            start=1
        ):

            payment_rows += f"""
            <tr>

                <td>
                    {index}
                </td>

                <td>
                    ₹{float(
                        payment["installment_amount"]
                    ):,.2f}
                </td>

                <td>
                    {payment["payment_date"]}
                </td>

                <td>
                    {payment["payment_status"]}
                </td>

            </tr>
            """


        receipt_html = f"""
        <div class="receipt">

            {stamp_html}

            <div class="receipt-header">

                <h1>
                    {INSTITUTE_NAME}
                </h1>

                <p>
                    {TAGLINE}
                </p>

                <h3>
                    ADMISSION RECEIPT
                </h3>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Admission ID
                </span>

                <span class="receipt-value">
                    {student["admission_id"]}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Date
                </span>

                <span class="receipt-value">
                    {student["created_at"]}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Student Name
                </span>

                <span class="receipt-value">
                    {student["name"]}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Mobile
                </span>

                <span class="receipt-value">
                    {student["phone"]}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Email
                </span>

                <span class="receipt-value">
                    {student["email"] or "-"}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Course
                </span>

                <span class="receipt-value">
                    {student["course"]}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Batch
                </span>

                <span class="receipt-value">
                    {student["batch"] or "-"}
                </span>

            </div>


            <div class="receipt-row">

                <span class="receipt-label">
                    Mode
                </span>

                <span class="receipt-value">
                    {student["mode"] or "-"}
                </span>

            </div>


            <br>


            <h3>
                Payment History
            </h3>


            <table style="
                width:100%;
                border-collapse:collapse;
                margin-top:15px;
            ">

                <thead>

                    <tr style="
                        background:#fff7ed;
                    ">

                        <th style="
                            padding:10px;
                            border:1px solid #ddd;
                        ">
                            Installment
                        </th>

                        <th style="
                            padding:10px;
                            border:1px solid #ddd;
                        ">
                            Amount
                        </th>

                        <th style="
                            padding:10px;
                            border:1px solid #ddd;
                        ">
                            Date
                        </th>

                        <th style="
                            padding:10px;
                            border:1px solid #ddd;
                        ">
                            Status
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {payment_rows}

                </tbody>

            </table>


            <div class="total-box">

                <h3>
                    Total Verified Amount:
                    ₹{verified_total:,.2f}
                </h3>

                <p>
                    Pending Amount:
                    ₹{pending_total:,.2f}
                </p>

                <p>
                    Rejected Amount:
                    ₹{rejected_total:,.2f}
                </p>

            </div>


            <br>


            <p>
                <strong>
                    TechScaler Solutions
                </strong>
            </p>

            <p>
                {ADDRESS}
            </p>

            <p>
                Mobile: {PHONE}
            </p>

            <p>
                Email: {EMAIL}
            </p>

            <p>
                Website: {WEBSITE}
            </p>

            <p style="
                color:#6b7280;
                font-size:12px;
            ">
                This is a system-generated admission receipt.
            </p>

        </div>
        """


        st.markdown(
            receipt_html,
            unsafe_allow_html=True
        )


        if has_verified_payment:

            st.success(
                "✓ Payment Verified — PAID / VERIFIED stamp displayed."
            )

        else:

            st.warning(
                "Payment verification is pending. "
                "The PAID / VERIFIED stamp will appear after admin verification."
            )


        st.info(
            "To save this receipt as PDF, use your browser's "
            "Print → Save as PDF option."
        )


        if st.button(
            "❌ Close Receipt",
            use_container_width=True
        ):

            st.session_state.receipt_id = None

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
    <div class="footer">

        <strong>
            {INSTITUTE_NAME}
        </strong>

        <br><br>

        {TAGLINE}

        <br><br>

        📞 {PHONE}
        &nbsp; | &nbsp;
        ✉️ {EMAIL}

        <br><br>

        {ADDRESS}

        <br><br>

        © {datetime.now().year}
        {INSTITUTE_NAME}

    </div>
    """,
    unsafe_allow_html=True
)