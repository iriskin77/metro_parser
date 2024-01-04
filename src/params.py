url = 'https://api.metro-cc.ru/products-api/graph'

cookies = {
    '_ga_VHKD93V3FV': 'GS1.1.1704187975.25.1.1704188636.0.0.0',
    '_ga': 'GA1.1.1776648454.1702151302',
    '_slid': '6574c48650021ed0e50aafc1',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1704195175%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1704195175%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1703405656%3B649ea9cb5bdadc85d50474f9%3A6576eb93a7daa0533002a0cf%3A1703417582',
    'uxs_uid': 'e9264170-96cb-11ee-a825-2790ef47fbcb',
    '_gcl_au': '1.1.814209504.1702151305',
    'mindboxDeviceUUID': 'c6900f50-2e57-48bb-9c3d-97e6f1cdff83',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22c6900f50-2e57-48bb-9c3d-97e6f1cdff83%22%7D',
    'tmr_lvid': '0351a42ebec541e9922554cb8aee859b',
    'tmr_lvidTS': '1702151304821',
    '_slid_server': '6574c48650021ed0e50aafc1',
    'metro_api_session': 'PCmORjuEFB4paTBXwX6pE7jvGewRAThQDtY84Wl9',
    '_slsession': '826B21D4-DD3A-4ED4-8AE3-FF46A2EC15FA',
    'mp_88875cfb7a649ab6e6e310368f37a563_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18c501fb3391ce4-022216f37c8f778-47380724-1a9640-18c501fb3391ce4%22%2C%22%24device_id%22%3A%20%2218c501fb3391ce4-022216f37c8f778-47380724-1a9640-18c501fb3391ce4%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://online.metro-cc.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://online.metro-cc.ru/',
    # 'Cookie': '_ga_VHKD93V3FV=GS1.1.1704187975.25.1.1704188636.0.0.0; _ga=GA1.1.1776648454.1702151302; _slid=6574c48650021ed0e50aafc1; _slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1704195175%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1704195175%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1703405656%3B649ea9cb5bdadc85d50474f9%3A6576eb93a7daa0533002a0cf%3A1703417582; uxs_uid=e9264170-96cb-11ee-a825-2790ef47fbcb; _gcl_au=1.1.814209504.1702151305; mindboxDeviceUUID=c6900f50-2e57-48bb-9c3d-97e6f1cdff83; directCrm-session=%7B%22deviceGuid%22%3A%22c6900f50-2e57-48bb-9c3d-97e6f1cdff83%22%7D; tmr_lvid=0351a42ebec541e9922554cb8aee859b; tmr_lvidTS=1702151304821; _slid_server=6574c48650021ed0e50aafc1; metro_api_session=PCmORjuEFB4paTBXwX6pE7jvGewRAThQDtY84Wl9; _slsession=826B21D4-DD3A-4ED4-8AE3-FF46A2EC15FA; mp_88875cfb7a649ab6e6e310368f37a563_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18c501fb3391ce4-022216f37c8f778-47380724-1a9640-18c501fb3391ce4%22%2C%22%24device_id%22%3A%20%2218c501fb3391ce4-022216f37c8f778-47380724-1a9640-18c501fb3391ce4%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'query': '\n  query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\n    category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {\n      id\n      name\n      slug\n      id\n      parent_id\n      meta {\n        description\n        h1\n        title\n        keywords\n      }\n      disclaimer\n      description {\n        top\n        main\n        bottom\n      }\n#      treeBranch {\n#        id\n#        name\n#        slug\n#        children {\n#          category_type\n#          id\n#          name\n#          slug\n#          children {\n#            category_type\n#            id\n#            name\n#            slug\n#            children {\n#              category_type\n#              id\n#              name\n#              slug\n#              children {\n#                category_type\n#                id\n#                name\n#                slug\n#              }\n#            }\n#          }\n#        }\n#      }\n      breadcrumbs {\n        category_type\n        id\n        name\n        parent_id\n        parent_slug\n        slug\n      }\n      promo_banners {\n        id\n        image\n        name\n        category_ids\n        virtual_ids\n        type\n        sort_order\n        url\n        is_target_blank\n        analytics {\n          name\n          category\n          brand\n          type\n          start_date\n          end_date\n        }\n      }\n\n\n      dynamic_categories(from: 0, size: 9999) {\n        slug\n        name\n        id\n        category_type\n      }\n      filters {\n        facets {\n          key\n          total\n          filter {\n            id\n            name\n            display_title\n            is_list\n            is_main\n            text_filter\n            is_range\n            category_id\n            category_name\n            values {\n              slug\n              text\n              total\n            }\n          }\n        }\n      }\n      total\n      prices {\n        max\n        min\n      }\n      pricesFiltered {\n        max\n        min\n      }\n      products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters)  {\n        health_warning\n        limited_sale_qty\n        id\n        slug\n        name\n        name_highlight\n        article\n        main_article\n        main_article_slug\n        is_target\n        category_id\n        url\n        images\n        pick_up\n        rating\n        icons {\n          id\n          badge_bg_colors\n          rkn_icon\n          caption\n          image\n          type\n          is_only_for_sales\n          stores\n          caption_settings {\n            colors\n            text\n          }\n          stores\n          sort\n          image_png\n          image_svg\n          description\n          end_date\n          start_date\n          status\n        }\n        manufacturer {\n          id\n          image\n          name\n        }\n        packing {\n          size\n          type\n          pack_factors {\n            instamart\n          }\n        }\n        stocks {\n          value\n          text\n          eshop_availability\n          scale\n          prices_per_unit {\n            old_price\n            offline {\n              price\n              old_price\n              type\n              offline_discount\n              offline_promo\n            }\n            price\n            is_promo\n            levels {\n              count\n              price\n            }\n            online_levels {\n              count\n              price\n              discount\n            }\n            discount\n          }\n          prices {\n            price\n            is_promo\n            old_price\n            offline {\n              old_price\n              price\n              type\n              offline_discount\n              offline_promo\n            }\n            levels {\n              count\n              price\n            }\n            online_levels {\n              count\n              price\n              discount\n            }\n            discount\n          }\n        }\n      }\n    }\n  }\n',
    'variables': {
        'isShouldFetchOnlyProducts': True,
        'slug': 'konfety-podarochnye-nabory',
        'storeId': 30,
        'sort': 'default',
        'size': 580,
        'from': 0,
        'filters': [
            {
                'field': 'main_article',
                'value': '0',
            },
        ],
        'attributes': [],
        'in_stock': False,
        'eshop_order': False,
    },
}
