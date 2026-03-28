import re
import os

filepath = r"c:\Users\Lenovo\OneDrive\Desktop\movie-portal - Copy\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Make the navigation links active
html = re.sub(r'<a href="#"([^>]*?)>Home</a>', r'<a href="index.html"\1>Home</a>', html)
html = re.sub(r'<a href="#"([^>]*?)>Articles</a>', r'<a href="articles.html"\1>Articles</a>', html)

# Author profile
html = re.sub(r'(Alex Developer)</p>', r'<a href="author-profile.html" class="hover:text-primary transition-colors">\1</a></p>', html)

# Headings
html = re.sub(r'(1\. The Core Foundation)</h2>', r'<a href="core-foundation.html" class="hover:text-primary transition-colors block">\1</a></h2>', html)
html = re.sub(r'(1\.1 Infrastructure as a Service \(IaaS\))</h3>', r'<a href="iaas.html" class="hover:text-primary transition-colors block">\1</a></h3>', html)
html = re.sub(r'(2\. The Role of Virtualization)</h2>', r'<a href="virtualization.html" class="hover:text-primary transition-colors block">\1</a></h2>', html)
html = re.sub(r'(Why Microservices\?)\s*</h4>', r'<a href="microservices.html" class="hover:text-primary transition-colors block">\1</a></h4>', html)
html = re.sub(r'(3\. Security and Networking)</h2>', r'<a href="security-networking.html" class="hover:text-primary transition-colors block">\1</a></h2>', html)
html = re.sub(r'(3\.1 Identity Management)</h3>', r'<a href="identity-management.html" class="hover:text-primary transition-colors block">\1</a></h3>', html)
html = re.sub(r'(3\.2 Global Load Balancing)</h3>', r'<a href="load-balancing.html" class="hover:text-primary transition-colors block">\1</a></h3>', html)

# Footer
html = re.sub(r'<a href="#" class="(.*?)">Privacy Policy</a>', r'<a href="privacy-policy.html" class="\1">Privacy Policy</a>', html)
html = re.sub(r'<a href="#" class="(.*?)">Terms of Service</a>', r'<a href="terms-of-service.html" class="\1">Terms of Service</a>', html)

# Aside Buttons
for btn in re.findall(r'<button\s+class="w-full group flex [\s\S]*?</button>', html):
    if 'Cloud\n' in btn:
        new_btn = btn.replace('<button', '<a href="cloud-computing.html"').replace('</button>', '</a>')
        html = html.replace(btn, new_btn)
    elif 'Cyber\n' in btn:
        new_btn = btn.replace('<button', '<a href="cyber-security.html"').replace('</button>', '</a>')
        html = html.replace(btn, new_btn)
    elif 'Web\n' in btn:
        new_btn = btn.replace('<button', '<a href="web-development.html"').replace('</button>', '</a>')
        html = html.replace(btn, new_btn)
    elif 'Analytics' in btn:
        new_btn = btn.replace('<button', '<a href="ai-analytics.html"').replace('</button>', '</a>')
        html = html.replace(btn, new_btn)

# Write updated index.html
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

# Now extract templates
head_match = re.search(r'([\s\S]*?)<div class="lg:col-span-2">', html)
head_part = head_match.group(1) + '<div class="lg:col-span-2">\n'

foot_match = re.search(r'(        <aside class="lg:col-span-1 space-y-8">[\s\S]*)', html)
foot_part = '        </div>\n\n' + foot_match.group(1)

pages = [
    ("articles.html", "Articles", "All Articles", "Browse our comprehensive directory of technical articles covering cloud, security, and development."),
    ("cloud-computing.html", "Cloud Computing", "Cloud Computing", "Explore the fundamentals and advanced concepts of cloud infrastructure."),
    ("cyber-security.html", "Cyber Security", "Cyber Security", "Learn about the latest threats and how to secure your digital assets."),
    ("web-development.html", "Web Development", "Web Development", "Master modern web development frameworks and architectures."),
    ("ai-analytics.html", "AI & Analytics", "AI & Analytics", "Dive deep into machine learning models and data analytics strategies."),
    ("core-foundation.html", "The Core Foundation", "The Core Foundation", "Detailed breakdown of the physical and virtual components that make up cloud computing."),
    ("iaas.html", "Infrastructure as a Service", "Infrastructure as a Service (IaaS)", "How IaaS abstracts physical hardware into scalable, virtualized resources."),
    ("virtualization.html", "The Role of Virtualization", "The Role of Virtualization", "At the core of cloud architectures is the hypervisor, splitting hardware into secure environments."),
    ("microservices.html", "Why Microservices?", "Why Microservices?", "Deploying applications rapidly as microservices enhances fault tolerance and portability."),
    ("security-networking.html", "Security and Networking", "Security and Networking", "Effective cloud architectures integrate robust networking topologies and telemetric monitoring."),
    ("identity-management.html", "Identity Management", "Identity Management", "Integrating robust identity and access management (IAM) ensures secure cloud environments."),
    ("load-balancing.html", "Global Load Balancing", "Global Load Balancing", "Virtual Private Clouds (VPCs) and load balancers work in tandem to ensure five-nines availability."),
    ("privacy-policy.html", "Privacy Policy", "Privacy Policy", "Our commitment to protecting your privacy and digital footprint."),
    ("terms-of-service.html", "Terms of Service", "Terms of Service", "The rules and regulations for using Technical Knowledge Hub."),
    ("author-profile.html", "Profile: Alex Developer", "Alex Developer", "Cloud Systems Architect with over a decade of experience in building scalable systems."),
    ("saas-paas.html", "SaaS and PaaS", "Software and Platform as a Service", "Beyond IaaS: Exploring higher-level cloud abstraction models."),
    ("containerization.html", "Containerization", "Containerization Ecosystems", "Deep dive into Docker, Kubernetes, and container orchestration."),
    ("zero-trust-security.html", "Zero Trust Security", "Zero Trust Security", "Never trust, always verify: Implementing modern security postures."),
    ("cloud-migrations.html", "Cloud Migrations", "Cloud Migrations", "Strategies and best practices for migrating legacy applications to the cloud."),
    ("about-us.html", "About Us", "About Technical Knowledge Hub", "Learn more about our mission to empower developers around the world."),
    ("contact.html", "Contact", "Contact Us", "Get in touch with our editorial team for inquiries, feedback, and collaboration."),
    ("cookie-policy.html", "Cookie Policy", "Cookie Policy", "Information about how we use cookies to improve your browsing experience.")
]

for filename, title, heading, desc in pages:
    page_content = f"""
            <header class="mb-10 sm:mb-12">
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4 leading-tight">
                    {heading}
                </h1>
                <h2 class="text-xl sm:text-2xl font-medium text-slate-500 mb-8 leading-snug">
                    {desc}
                </h2>
                <div class="flex items-center gap-4 py-6 border-y border-slate-200">
                    <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-primary to-blue-400 shadow flex items-center justify-center">
                        <span class="text-white font-bold text-lg">TK</span>
                    </div>
                    <div>
                        <p class="text-slate-900 text-base font-semibold">TechHub Editors</p>
                        <p class="text-sm text-slate-500">Content Team</p>
                    </div>
                </div>
            </header>
            <article class="prose prose-slate max-w-none text-slate-600 text-base sm:text-lg leading-relaxed sm:leading-loose min-h-[400px]">
                <p>Welcome to <strong>{title}</strong>. Detailed comprehensive content for this topic is currently being developed by our subject matter experts. Please check back soon for the full article.</p>
                <div class="bg-blue-50 rounded-2xl p-6 sm:p-8 border border-blue-100 my-10 shadow-sm relative overflow-hidden">
                    <div class="absolute top-0 left-0 w-1 h-full bg-primary"></div>
                    <h4 class="text-slate-900 font-bold text-lg mb-3">Stay Updated</h4>
                    <p class="text-sm sm:text-base text-slate-700 m-0">Join our community newsletter to get notified when this guide is fully published and available!</p>
                </div>
                <div class="mt-8 pt-8 border-t border-slate-200">
                    <a href="index.html" class="inline-flex items-center justify-center px-6 py-3 border border-slate-300 shadow-sm text-base font-medium rounded-xl text-slate-700 bg-white hover:bg-slate-50 hover:text-primary transition-all duration-200 gap-2">
                        &larr; Back to Home Dashboard
                    </a>
                </div>
            </article>
"""
    # Replace title tag in head
    page_head = re.sub(r'<title>.*?</title>', f'<title>{title} | TechHub</title>', head_part)
    
    out_filepath = os.path.join(r"c:\Users\Lenovo\OneDrive\Desktop\movie-portal - Copy", filename)
    with open(out_filepath, 'w', encoding='utf-8') as f:
        f.write(page_head + page_content + foot_part)

print(f"Update script completed. Generated {len(pages)} pages.")
