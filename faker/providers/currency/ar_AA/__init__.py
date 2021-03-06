from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # Format: (code, name)
    currencies = (
        ("AED", "درهم إماراتي"),
        ("AFN", "أفغاني"),
        ("ALL", "ليك ألباني"),
        ("AMD", "درام أرميني"),
        ("ANG", "غيلدر الأنتيل الهولندية"),
        ("AOA", "كوانزا أنغولي"),
        ("ARS", "بيزو أرجنتيني"),
        ("AUD", "دولار أسترالي"),
        ("AWG", "فلورن أروبي"),
        ("AZN", "مانات أذربيجاني"),
        ("BAM", "مارك بوسني"),
        ("BBD", "دولار بربادوسي"),
        ("BDT", "تاكا بنغلاديشي"),
        ("BGN", "ليف بلغاري"),
        ("BHD", "دينار بحريني"),
        ("BIF", "فرنك بوروندي"),
        ("BMD", "دولار برمودي"),
        ("BND", "دولار بروني"),
        ("BOB", "بوليفاريو بوليفي"),
        ("BRL", "ريال برازيلي"),
        ("BSD", "دولار بهامي"),
        ("BTN", "نغولترم بوتاني"),
        ("BWP", "بولا بوتسواني"),
        ("BYR", "روبل بيلاروسي"),
        ("BZD", "دولار بليزي"),
        ("CAD", "دولار كندي"),
        ("CDF", "فرنك كونغولي"),
        ("CHF", "فرنك سويسري"),
        ("CLP", "بيزو تشيلي"),
        ("CNY", "يوان"),
        ("COP", "بيزو كولومبي"),
        ("CRC", "كولون كوستاريكي"),
        ("CUC", "بيزو كوبي قابل للتحويل"),
        ("CUP", "بيزو كوبي"),
        ("CVE", "إيسكودو جزر الرأس الأخضر"),
        ("CZK", "كرونة تشيكية"),
        ("DJF", "فرنك جيبوتي"),
        ("DKK", "كرونة دنماركية"),
        ("DOP", "بيزو دومنيكاني"),
        ("DZD", "دينار جزائري"),
        ("EGP", "جنيه مصري"),
        ("ERN", "ناكفا"),
        ("ETB", "بير إثيوبي"),
        ("EUR", "يورو"),
        ("FJD", "دولار فيجي"),
        ("FKP", "جنيه جزر فوكلاند"),
        ("GBP", "جنيه إسترليني"),
        ("GEL", "لاري جورجي"),
        ("GGP", "جنيه جيرنزي"),
        ("GHS", "سيدي غاني"),
        ("GIP", "جنيه جبل طارق"),
        ("GMD", "دالاسي غامبي"),
        ("GNF", "فرنك غيني"),
        ("GTQ", "كتزال غواتيمالي"),
        ("GYD", "دولار غياني"),
        ("HKD", "دولار هونغ كونغ"),
        ("HNL", "لمبيرة هندوراسية"),
        ("HRK", "كونا كرواتية"),
        ("HTG", "جوردة هايتية"),
        ("HUF", "فورنت مجري"),
        ("IDR", "روبية إندونيسية"),
        ("ILS", "شيكل إسرائيلي"),
        ("NIS", "شيكل إسرائيلي جديد"),
        ("IMP", "جنيه مانكس"),
        ("INR", "روبية هندية"),
        ("IQD", "دينار عراقي"),
        ("IRR", "ريال إيراني"),
        ("ISK", "كرونة آيسلندية"),
        ("JEP", "جنيه جيرزي"),
        ("JMD", "دولار جامايكي"),
        ("JOD", "دينار أردني"),
        ("JPY", "ين ياباني"),
        ("KES", "شيلينغ كيني"),
        ("KGS", "سوم قيرغيزستاني"),
        ("KHR", "ريال كمبودي"),
        ("KMF", "فرنك قمري"),
        ("KPW", "وون كوري شمالي"),
        ("KRW", "وون كوري جنوبي"),
        ("KWD", "دينار كويتي"),
        ("KYD", "دولار جزر كايمان"),
        ("KZT", "تينغ كازاخستاني"),
        ("LAK", "كيب لاوي"),
        ("LBP", "ليرة لبنانية"),
        ("LKR", "روبية سريلانكي"),
        ("LRD", "دولار ليبيري"),
        ("LSL", "لوتي ليسوتو"),
        ("LTL", "الليتاس اللتواني"),
        ("LYD", "دينار ليبي"),
        ("MAD", "درهم مغربي"),
        ("MDL", "ليو مولدوفي"),
        ("MGA", "أرياري مدغشقري"),
        ("MKD", "دينار مقدوني"),
        ("MMK", "كيات ميانماري"),
        ("MNT", "توغروغ منغولي"),
        ("MOP", "باتاكا ماكاوية"),
        ("MRO", "أوقية موريتانية"),
        ("MUR", "روبي موريشي"),
        ("MVR", "روفيه مالديفية"),
        ("MWK", "كواشا ملاوية"),
        ("MXN", "بيزو مكسيكي"),
        ("MYR", "رينغيت ماليزي"),
        ("MZN", "متكال موزمبيقي"),
        ("NAD", "دولار ناميبي"),
        ("NGN", "نيرة نيجيرية"),
        ("NIO", "كوردبا نيكاراغوا"),
        ("NOK", "كرونة نروجية"),
        ("NPR", "روبية نيبالية"),
        ("NZD", "دولار نيوزيلندي"),
        ("OMR", "ريال عماني"),
        ("PAB", "بالبوا بنمي"),
        ("PEN", "سول بيروفي"),
        ("PGK", "كينا بابوا غينيا الجديدة"),
        ("PHP", "بيسو فلبيني"),
        ("PKR", "روبية باكستانية"),
        ("PLN", "زلوتي بولندي"),
        ("PYG", "غواراني باراغواي"),
        ("QAR", "ريال قطري"),
        ("RON", "ليو روماني"),
        ("RSD", "دينار صربي"),
        ("RUB", "روبل روسي"),
        ("RWF", "فرنك رواندي"),
        ("SAR", "ريال سعودي"),
        ("SBD", "دولار جزر سليمان"),
        ("SCR", "روبية سيشلية"),
        ("SDG", "جنيه سوداني"),
        ("SEK", "كرونة سويدية"),
        ("SGD", "دولار سنغافوري"),
        ("SHP", "جنيه سانت هيليني"),
        ("SLL", "ليون سيراليوني"),
        ("SOS", "شلن صومالي"),
        ("SPL", "لويجينو"),
        ("SRD", "دولار سورينامي"),
        ("STD", "دوربا ساو توميان"),
        ("SVC", "كولون سلفادوري"),
        ("SYP", "ليرة سورية"),
        ("SZL", "ليلانغيني سوازيلندي"),
        ("THB", "بات تايلاندي"),
        ("TJS", "ساماني طاجيكي"),
        ("TMT", "منات تركمانستاني"),
        ("TND", "دينار تونسي"),
        ("TOP", "بانغا تونغي"),
        ("TRY", "ليرة تركية"),
        ("TTD", "دولار ترينيداد وتوباغو"),
        ("TVD", "دولار توفالو"),
        ("TWD", "دولار تايواني جديد"),
        ("TZS", "شيلينغ تانزاني"),
        ("UAH", "هريفنا أوكرانية"),
        ("UGX", "شيلينغ أوغندي"),
        ("USD", "دولار أمريكي"),
        ("UYU", "بيزو أوروغواي"),
        ("UZS", "سوم أوزبكستاني"),
        ("VEF", "بوليفار فنزويلي"),
        ("VND", "دونغ فيتنامي"),
        ("VUV", "فاتو فانواتي"),
        ("WST", "تالا ساموي"),
        ("XAF", "فرنك وسط أفريقي"),
        ("XCD", "دولار شرق الكاريبي"),
        ("XDR", "حقوق السحب الخاصة"),
        ("XOF", "فرنك غرب أفريقي"),
        ("XPF", "فرنك س ف ب"),
        ("YER", "ريال يمني"),
        ("ZAR", "راند جنوب أفريقي"),
        ("ZMW", "كواشا زامبي"),
        ("ZWD", "دولار زيمبابوي"),
    )
