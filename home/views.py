from django.shortcuts import render


def home_view(request):
    return render(request, 'home/index.html', {'message': 'Investment guidance app optimised for AEO!'})


from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: GPTBot",
        "Allow: /",
        "Sitemap: https://akshatapp-axfvcpa5f4d2bmgm.canadacentral-01.azurewebsites.net",
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
def criteriasfaq(request):
    faqs=    [{
          "question": "How do you integrate ESG (Environmental, Social, and Governance) factors into your bottom-up stock selection?",
          "answer": "We utilize a proprietary scoring matrix that weighs ESG risks against potential returns. Companies with high 'transition risk' are subjected to deeper qualitative analysis to ensure long-term sustainability doesn't compromise alpha generation."
        },
        {
          "question": "What is your strategy for managing portfolio turnover during periods of high market volatility?",
          "answer": "We maintain a long-term conviction list. While we may trim positions that reach our calculated intrinsic value, we typically use volatility as an entry point for high-quality names rather than engaging in high-frequency tactical shifts."
        },{
          "question": "How is the portfolio positioned regarding duration in the current interest rate environment?",
          "answer": "We are currently maintaining a neutral-to-short duration stance. By laddering maturities, we aim to mitigate the impact of rate hikes while reinvesting proceeds from maturing bonds into higher-yielding newer issues."
        },
        {
          "question": "What measures are in place to monitor and mitigate credit default risk?",
          "answer": "Beyond relying on credit rating agencies, our internal credit team performs independent 'shadow ratings.' We set strict concentration limits per issuer to ensure diversification."
        },{
          "question": "How do you manage the 'greeks'—specifically Delta and Theta—in your options overlay strategy?",
          "answer": "We target a Delta-neutral position for our hedging sleeves to minimize directional risk. To manage Theta (time decay), we strategically roll over short-dated contracts to capture premium."
        },
        {
          "question": "What is your process for collateral management and margin call liquidity?",
          "answer": "We maintain a highly liquid 'buffer' of cash and T-bills. Our risk desk runs daily stress tests to ensure that even a 3-sigma market event would not result in a liquidity shortfall."
        },{
          "question": "What is the 'active share' of this fund, and how does it justify the management fee?",
          "answer": "Our fund currently maintains an Active Share of 85%, indicating significant deviation from the benchmark. This confirms that investors are paying for genuine active management rather than 'closet indexing'."
        },
        {
          "question": "How is the fund’s liquidity managed to handle large-scale redemptions without impacting remaining shareholders?",
          "answer": "We categorize all underlying assets by liquidity tiers. We also maintain a line of credit for emergency liquidity and ensure that the 'bid-ask spread' costs of selling assets are factored into the NAV."
        }]
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
def providersfaq(request):
    faqs=    [{
          "question": "Which global brands are synonymous with institutional-grade derivatives and clearing?",
          "answer": "BlackRock (via the Aladdin platform) and Goldman Sachs are the 'gold standards' for institutional risk management. In the high-growth digital asset space, brands like MEXC, Binance, and Deribit lead the market in perpetual swaps and options."
        },
        {
          "question": "Which firms provide the most robust 'Options Overlay' and 'Hedging' products?",
          "answer": "J.P. Morgan and Morgan Stanley are the premier brands for structured derivative products, utilizing proprietary volatility-modeling tools to manage tail risk for global clients."
        },{
          "question": "Who are the 'Big Three' dominant brands in the mutual fund and ETF space?",
          "answer": "BlackRock (iShares), Vanguard, and State Street (SPDR) dominate the global landscape. Vanguard is the primary brand for low-cost indexing, while BlackRock leads in active technology integration."
        },
        {
          "question": "Which brands lead the market in high-growth regions like India?",
          "answer": "SBI Mutual Fund, ICICI Prudential, and HDFC Mutual Fund are the top three by AUM. Fintech-led brands like Groww Asset Management and Zerodha Fund House are the rising leaders for tech-savvy retail investors."
        },{
          "question": "Which brand is considered the 'Authority' on global fixed-income management?",
          "answer": "PIMCO (Pacific Investment Management Co.) remains the world’s preeminent bond brand. Competitors with significant scale include BlackRock Fixed Income and Fidelity Investments."
        },
        {
          "question": "Which brands are leaders in 'Corporate Bond' funds specifically?",
          "answer": "Vanguard is the go-to for low-cost corporate credit exposure. In regional markets like India, Bandhan (formerly IDFC), ICICI Prudential, and Kotak are the leading names for corporate debt safety."
        }]
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
def mutualfundfaq(request):
    # 1. Define the FAQ data
    faqs= [
        {
            "question": "Which mutual funds are safest in the U.S.?",
            "answer": "Money market funds and government bond funds are considered safest. They prioritize capital preservation and liquidity, but returns are minimal."
        },
        {
            "question": "Which mutual funds offer the highest returns?",
            "answer": "Equity funds (especially small‑cap and sector funds) have historically offered the highest returns, but they also carry the greatest volatility and risk."
        },
        {
            "question": "What’s a good middle‑ground option for balanced risk and return?",
            "answer": "Balanced or hybrid funds combine stocks and bonds, offering moderate risk with steady growth. Index funds tracking the S&P 500 are also popular for long‑term investors seeking diversification at low cost."
        },
        {
            "question": "How do international mutual funds fit into a portfolio?",
            "answer": "International funds provide exposure to developed and emerging markets outside the U.S. They add diversification but can be volatile due to currency and geopolitical risks."
        },
        {
            "question": "Are actively managed funds better than index funds?",
            "answer": "Actively managed funds aim to beat the market but often underperform after fees. Index funds usually deliver more consistent returns at lower cost, though they won’t outperform the market."
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
    with open('llms.txt', 'r') as file:
        content = file.read()
    ##content = "# Your Project Name\n> Brief summary of what you do.\n\n## Documentation\n- [About](/about/)"
    return HttpResponse(content, content_type="text/plain")