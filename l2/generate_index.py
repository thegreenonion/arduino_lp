import markdown

# Markdown-Datei einlesen
with open('Readme.md', 'r') as f:
    markdown_text = f.read()

# Vorlage für eine einzelne jQuery Mobile-Seite einlesen
with open('seiten_vorlage.html', 'r') as f:
    html_vorlage = f.read()

# Markdown-Text in Sektionen aufteilen und in separate jQuery Mobile-Seiten einfügen
pages = []
sektionen = markdown_text.split('\n## ')[1:]

def create_panel_links(sektionen):
    links = []

    for j, sektion in enumerate(sektionen):
        page_id = f"page{j}"
        sektion_title, sektion_text = sektion.split('\n', 1)
        if i == j:
            links.append(f'<li><a href="#{page_id}">> {sektion_title}</a></li>')
            continue
        links.append(f'<li><a href="#{page_id}">{sektion_title}</a></li>')
    return links

for i, sektion in enumerate(sektionen):
    sektionen_html = markdown.markdown("## " + sektion)

    links = create_panel_links(sektionen)

    sektion_title, sektion_text = sektion.split('\n', 1)
    page_id = f"page{i}"
    next_page_id = f"page{i + 1}"
    panel_id = f"panel{i}"

    page = f"""
    <div data-role="page" id="{page_id}">
        <div data-role="header" data-theme="b">
            <h1></h1>
            <a href="#" data-rel="back" data-icon="back" data-iconpos="notext"></a>
            <a href="#{panel_id}" data-icon="bars" data-iconpos="notext">Menu</a>
        </div>
        <div data-role="content">
            {sektionen_html}
            <a href="#{next_page_id}" data-role="button" data-theme="b">Weiter</a>
        </div>
        <div data-role="panel" id="{panel_id}" data-position="right" data-display="overlay" data-theme="b">
            <ul data-role="listview">
                {''.join(links)}
            </ul>
        </div>
        <div data-role="footer" data-position="fixed" data-theme="b">
	        <h3>{i} / {len(sektionen)}</h3>
        </div>
    </div>
    """
    pages.append(page)

html_seite = html_vorlage.replace('{{inhalt}}', "\n".join(pages))
with open(f'data/index.html', 'w') as f:
    f.write(html_seite)
