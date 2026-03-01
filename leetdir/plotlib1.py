import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Years
    years = [2016, 2019, 2020, 2023]

    # GDP per capita data (nominal USD)
    alabama_gdp = [42344, 46924, 46756, 59585]
    canada_gdp  = [42382, 46431, 43573, 54517]
    years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
             2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
             2020, 2021, 2022, 2023, 2024]

    # GDP per capita data (nominal USD)
    alabama_gdp = [37291, 38004, 38901, 39871, 40318, 41374, 42344, 36861, 37019, 35914,
                   37073, 38649, 40112, 41863, 42928, 41374, 42344, 43812, 45231, 46924,
                   46756, 51497, 56135, 59585, 61012]

    canada_gdp = [24271, 23742, 24133, 28091, 31941, 36105, 40285, 44452, 46370, 40643,
                  47561, 52086, 52669, 52635, 50962, 43594, 42382, 45129, 46548, 46353,
                  43538, 52887, 56257, 54220, 54283]

    jpyears = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

    # Bank of Japan policy / target rate (approximate annual average or year-end)
    boj_policy_rate = [
        -0.10,  # 2016 – negative rate policy in place (introduced in Jan 2016)
        -0.10,  # 2017 – unchanged negative rate
        -0.10,  # 2018 – unchanged
        -0.10,  # 2019 – unchanged
        -0.10,  # 2020 – unchanged, negative
        -0.10,  # 2021 – unchanged
        -0.10,  # 2022 – unchanged until early 2023
        -0.10,  # 2023 – negative rate right up to March
        0.00,
        # 2024 – first hike in March 2024 to 0%–0.1% range (ended negative rate regime) :contentReference[oaicite:0]{index=0}
        0.75  # 2025 – multiple hikes culminating in ~0.75% by December 2025 :contentReference[oaicite:1]{index=1}
    ]

    plt.figure(figsize=(8, 5))
    plt.plot(jpyears, boj_policy_rate, marker='o', label='BOJ rate changes')
    #plt.plot(years, canada_gdp, marker='s', label='Canada GDP per capita')

    plt.title('BOJ rates per year')
    plt.xlabel('Year')
    plt.ylabel('Rates')
    plt.grid(True)
    plt.legend()
    plt.show()