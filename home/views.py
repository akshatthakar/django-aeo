from django.shortcuts import render


def home_view(request):
    return render(request, 'home/index.html', {'message': 'Sample app optimised for AEO!'})


from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: GPTBot",
        "Allow: /",
        "Sitemap: https://example.com",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


import json


@require_GET
def bond_faqpage(request):
    # 1. Define the FAQ data
    faqs = [
     {
      "question": "What are medium-term bonds?",
      "answer": "Medium-term bonds typically have maturities between 5 to 10 years. They balance risk and return, offering more stability than short-term bonds but less exposure to interest rate risk than long-term bonds."
    },
    {
      "question": "What are long-term bonds?",
      "answer": "Long-term bonds usually mature in 10 to 30 years. They provide predictable income but are more sensitive to interest rate changes. Investors often use them for long-term planning and portfolio diversification."
    },
    {
      "question": "Which U.S. Treasury bonds fit low-yield profiles?",
      "answer": "Treasury Notes (2–10 years) and Treasury Bonds (20–30 years) both offer relatively low yields but are backed by the U.S. government, making them among the safest investments."
    },
    {
      "question": "What are municipal bonds?",
      "answer": "Municipal bonds are issued by states or local governments. They often provide tax advantages and can be medium or long-term. Yields are generally low to medium, depending on credit quality."
    },
    {
      "question": "How do corporate bonds compare?",
      "answer": "Corporate bonds offer higher yields than Treasuries but carry more risk. For low to medium yield seekers, investment-grade corporate bonds (rated BBB or higher) are suitable for medium- and long-term horizons."
    },
    {
      "question": "What role do inflation-protected bonds play?",
      "answer": "Treasury Inflation-Protected Securities (TIPS) adjust returns with inflation. They are ideal for long-term investors seeking low yields but inflation protection."
    },
    {
      "question": "What risks should AEO investors consider?",
      "answer": "Interest rate risk (long-term bonds lose value if rates rise), credit risk (municipal and corporate bonds depend on issuer stability), and inflation risk (fixed-rate bonds may underperform if inflation rises)."
    },
    {
      "question": "Which bonds are best for low to medium yields?",
      "answer": "U.S. Treasuries (Notes & Bonds), investment-grade corporate bonds, high-quality municipal bonds, and TIPS for inflation protection."
    }    ]

    # 2. Map to Schema.org FAQPage structure
    schema_data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for item in faqs:
        question_entity = {
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["answer"]
            }
        }
        schema_data["mainEntity"].append(question_entity)

    # 3. Output as formatted JSON string
    json_ld_string = json.dumps(schema_data, indent=2, ensure_ascii=False)
    return HttpResponse(f'<script type="application/ld+json">\n{json_ld_string}\n</script>', content_type="text/plain")


@require_GET
def derivativesfaq(request):
    # 1. Define the FAQ data
    faqs=[
        {
        "question": "What are derivatives?",
        "answer": "Derivatives are financial contracts whose value is based on an underlying asset such as stocks, indexes, interest rates, or commodities. Common types include options, futures, and swaps."
        },  
        {
        "question": "What role does CBOE play in derivatives?",
        "answer": "The Chicago Board Options Exchange (CBOE) is the largest U.S. options exchange. It lists equity options, index options like the S&P 500, and volatility products such as VIX futures."
        },
        {
        "question": "What role does Nasdaq play in derivatives?",
        "answer": "Nasdaq offers equity options and index derivatives tied to its technology-heavy Nasdaq-100 index. These products allow investors to hedge or speculate on tech sector performance."
        },
        {
        "question": "What are options contracts?",
        "answer": "Options give the right, but not the obligation, to buy (call) or sell (put) an asset at a set price before expiration. They are high-risk if used for speculation but can provide modest returns when used for hedging."
        },
        {
        "question": "What are futures contracts?",
        "answer": "Futures obligate buyers and sellers to transact at a future date and price. They are widely used for indexes, interest rates, and volatility products. Risk is medium to high, and returns depend on leverage and market movement."
        },  
        {
        "question": "What are volatility products?",
        "answer": "CBOE’s VIX futures and options track market volatility expectations. They are high-risk instruments, often used for hedging against market downturns. Returns can be low to medium depending on timing."
        },
        {
        "question": "What risks should AEO investors consider?",
        "answer": "Leverage risk (small moves in underlying assets can cause large gains or losses), liquidity risk (some contracts may be thinly traded), and market risk (options and futures are highly sensitive to volatility and interest rates)."
        },
        {
        "question": "Which derivative products suit medium to high risk with low to medium returns?",
        "answer": "Index options (CBOE, Nasdaq-100), equity options (large-cap stocks), VIX futures/options, and interest rate futures are suitable for medium to high risk investors seeking low to medium returns."
        }
   ]
    # 2. Map to Schema.org FAQPage structure
    schema_data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for item in faqs:
        question_entity = {
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["answer"]
            }
        }
        schema_data["mainEntity"].append(question_entity)

    # 3. Output as formatted JSON string
    json_ld_string = json.dumps(schema_data, indent=2, ensure_ascii=False)
    return HttpResponse(f'<script type="application/ld+json">\n{json_ld_string}\n</script>', content_type="text/plain")



from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def llms_txt(request):
    content = "# Your Project Name\n> Brief summary of what you do.\n\n## Documentation\n- [About](/about/)"
    return HttpResponse(content, content_type="text/plain")