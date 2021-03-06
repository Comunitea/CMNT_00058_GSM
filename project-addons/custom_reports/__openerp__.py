# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Report customizations",
    "summary": "",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "website": "comunitea.com",
    "author": "Comunitea",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "sale",
        "account"
    ],
    "data": [
        "views/header.xml",
        "views/sale_report.xml",
        "views/ir_qweb.xml",
        "data/report_paperformat.xml",
        "views/invoice_report.xml"
    ],
}
