import streamlit as st
import requests
import base64


# ============================================================
# TECHSCALER SOLUTIONS
# ADMISSION + INSTALLMENT FORM
# ============================================================

# Paste your Google Apps Script Web App URL here
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxM47zeAOS3qicXaiKWffmHkfG_r6vwtkLnZ1zdeZB7866XAQTMRo4hkX89xuW017-O/exec"


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="TechScaler Solutions | Admission Form",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .main {
        background-color: #f7f8fa;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .header-box {
        background: linear-gradient(
            135deg,
            #ff7a00,
            #ff9f43
        );
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }

    .header-title {
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .header-subtitle {
        font-size: 16px;
        opacity: 0.95;
    }

    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #222;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    .info-box {
        background: #fff7ed;
        border-left: 5px solid #ff7a00;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }

    .success-box {
        background: #ecfdf5;
        border-left: 5px solid #10b981;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }

    div[data-testid="stForm"] {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    }

    .footer {
        text-align: center;
        color: #777;
        margin-top: 30px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header-box">

    <div class="header-title">
        🎓 TechScaler Solutions
    </div>

    <div class="header-subtitle">
        Student Admission & Installment Payment Form
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INFORMATION
# ============================================================

st.markdown("""
<div class="info-box">

<b>📌 Important:</b><br>

Please enter the correct student details and upload
a clear screenshot of your payment transaction.

You can pay the course fees in multiple installments.

Example:
₹10,000 → First Installment<br>
₹5,000 → Second Installment<br>
₹5,000 → Third Installment

</div>
""", unsafe_allow_html=True)


# ============================================================
# ADMISSION FORM
# ============================================================

with st.form("admission_form"):

    # --------------------------------------------------------
    # STUDENT DETAILS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">👨‍🎓 Student Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        student_name = st.text_input(
            "Full Name *",
            placeholder="Enter student's full name"
        )

    with col2:

        mobile = st.text_input(
            "Mobile Number *",
            placeholder="Enter 10-digit mobile number"
        )

    col3, col4 = st.columns(2)

    with col3:

        email = st.text_input(
            "Email Address",
            placeholder="example@gmail.com"
        )

    with col4:

        mode = st.selectbox(
            "Learning Mode *",
            [
                "Online",
                "Offline",
                "Hybrid"
            ]
        )


    # --------------------------------------------------------
    # COURSE DETAILS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📚 Course Details</div>',
        unsafe_allow_html=True
    )

    col5, col6 = st.columns(2)

    with col5:

        course = st.selectbox(
            "Select Course *",
            [
                "Data Science",
                "Data Analytics",
                "Python",
                "Power BI",
                "SQL",
                "Machine Learning",
                "Generative AI",
                "R Programming",
                "Other"
            ]
        )

    with col6:

        batch = st.text_input(
            "Batch",
            placeholder="Example: Weekend / Weekday / Batch 01"
        )


    # --------------------------------------------------------
    # FEES
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">💰 Fees & Installment</div>',
        unsafe_allow_html=True
    )

    col7, col8 = st.columns(2)

    with col7:

        total_fees = st.number_input(
            "Total Course Fees (₹) *",
            min_value=1,
            step=1000,
            value=28000
        )

    with col8:

        installment_amount = st.number_input(
            "Current Installment Amount (₹) *",
            min_value=1,
            step=500,
            value=10000
        )


    # --------------------------------------------------------
    # PAYMENT INFORMATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">💳 Payment Details</div>',
        unsafe_allow_html=True
    )

    col9, col10 = st.columns(2)

    with col9:

        payment_mode = st.selectbox(
            "Payment Mode *",
            [
                "UPI",
                "Google Pay",
                "PhonePe",
                "Paytm",
                "Bank Transfer",
                "Cash",
                "Other"
            ]
        )

    with col10:

        transaction_id = st.text_input(
            "Transaction ID",
            placeholder="Enter transaction/reference ID"
        )


    # --------------------------------------------------------
    # PAYMENT SCREENSHOT
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📸 Payment Screenshot</div>',
        unsafe_allow_html=True
    )

    payment_file = st.file_uploader(
        "Upload Payment Screenshot *",
        type=[
            "png",
            "jpg",
            "jpeg",
            "webp"
        ],
        help="Upload a clear screenshot of your payment."
    )


    # --------------------------------------------------------
    # SUBMIT
    # --------------------------------------------------------

    submitted = st.form_submit_button(
        "🚀 Submit Admission",
        use_container_width=True
    )


# ============================================================
# FORM PROCESSING
# ============================================================

if submitted:

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not student_name.strip():

        st.error("❌ Please enter student name.")

        st.stop()


    if not mobile.strip():

        st.error("❌ Please enter mobile number.")

        st.stop()


    if not mobile.isdigit() or len(mobile) != 10:

        st.error(
            "❌ Please enter a valid 10-digit mobile number."
        )

        st.stop()


    if not course:

        st.error("❌ Please select a course.")

        st.stop()


    if total_fees <= 0:

        st.error("❌ Total fees must be greater than zero.")

        st.stop()


    if installment_amount <= 0:

        st.error(
            "❌ Installment amount must be greater than zero."
        )

        st.stop()


    if installment_amount > total_fees:

        st.error(
            "❌ Installment amount cannot exceed total fees."
        )

        st.stop()


    if payment_file is None:

        st.error(
            "❌ Please upload payment screenshot."
        )

        st.stop()


    # --------------------------------------------------------
    # FILE SIZE VALIDATION
    # --------------------------------------------------------

    max_size = 10 * 1024 * 1024

    if payment_file.size > max_size:

        st.error(
            "❌ File size must be less than 10 MB."
        )

        st.stop()


    # --------------------------------------------------------
    # READ FILE
    # --------------------------------------------------------

    file_bytes = payment_file.read()

    encoded_file = base64.b64encode(
        file_bytes
    ).decode("utf-8")


    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

    payload = {

        "name": student_name.strip(),

        "mobile": mobile.strip(),

        "email": email.strip(),

        "course": course,

        "batch": batch.strip(),

        "mode": mode,

        "totalFees": total_fees,

        "installmentAmount": installment_amount,

        "paymentMode": payment_mode,

        "transactionId": transaction_id.strip(),

        "fileName": payment_file.name,

        "mimeType": payment_file.type,

        "fileData": encoded_file

    }


    # --------------------------------------------------------
    # SEND TO GOOGLE APPS SCRIPT
    # --------------------------------------------------------

    if (
        GOOGLE_SCRIPT_URL ==
        "PASTE_YOUR_WEB_APP_URL_HERE"
    ):

        st.error(
            "❌ Please add your Google Apps Script Web App URL in app.py."
        )

        st.stop()


    try:

        with st.spinner(
            "Submitting admission and uploading payment proof..."
        ):

            response = requests.post(
                GOOGLE_SCRIPT_URL,
                json=payload,
                timeout=120
            )


        # ----------------------------------------------------
        # RESPONSE
        # ----------------------------------------------------

        if response.status_code != 200:

            st.error(
                f"❌ Server error: {response.status_code}"
            )

            st.stop()


        result = response.json()


        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        if result.get("success"):

            st.balloons()

            st.markdown(
                """
                <div class="success-box">

                <h2>✅ Admission Submitted Successfully!</h2>

                <p>
                Your admission/payment details have been
                successfully recorded.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


            # ------------------------------------------------
            # PAYMENT SUMMARY
            # ------------------------------------------------

            st.markdown("### 🧾 Payment Summary")


            col_a, col_b = st.columns(2)

            with col_a:

                st.metric(
                    "Admission ID",
                    result.get(
                        "admissionId",
                        "-"
                    )
                )

                st.metric(
                    "Installment No.",
                    result.get(
                        "installmentNo",
                        "-"
                    )
                )


            with col_b:

                st.metric(
                    "Current Payment",
                    f"₹{result.get('installmentAmount', 0):,.0f}"
                )

                st.metric(
                    "Total Paid",
                    f"₹{result.get('totalPaid', 0):,.0f}"
                )


            st.metric(
                "Remaining Amount",
                f"₹{result.get('remainingAmount', 0):,.0f}"
            )


            # ------------------------------------------------
            # FILE LINK
            # ------------------------------------------------

            file_url = result.get(
                "fileUrl",
                ""
            )

            if file_url:

                st.markdown(
                    f"""
                    🔗 **Payment Screenshot:**
                    [View Uploaded Screenshot]({file_url})
                    """
                )


            st.success(
                "🎉 Thank you for choosing TechScaler Solutions!"
            )


        else:

            st.error(
                "❌ " +
                result.get(
                    "message",
                    "Something went wrong."
                )
            )


    except requests.exceptions.Timeout:

        st.error(
            "❌ Request timed out. "
            "Please check Google Apps Script and try again."
        )


    except requests.exceptions.RequestException as e:

        st.error(
            f"❌ Connection error: {str(e)}"
        )


    except Exception as e:

        st.error(
            f"❌ Unexpected error: {str(e)}"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    © 2026 TechScaler Solutions<br>
    Data Science • Data Analytics • Python • Power BI • SQL • AI

    </div>
    """,
    unsafe_allow_html=True
)