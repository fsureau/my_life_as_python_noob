import os
from flask import Flask
import psycopg

app = Flask(__name__)


@app.route("/")
def hello():
    header = """
<div id="Outer">
<div id="Inner">
<h1>Lorem Ipsum</h1>
<h4>"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."</h4>
<h5>"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."</h5>


<hr>
"""
    content = """
<div id="Content">
<div id="bannerL"><!-- Tag ID: lipsumcom_left_siderail -->
<div align="center" data-freestar-ad="__300x600" id="lipsumcom_left_siderail" name="lipsumcom_left_siderail" data-google-query-id="CNL3p6TIwYEDFepfpAQdmEwC3A">
 <h1>Est ducimus numquam quo quia autem. </h1><p>Lorem ipsum dolor sit amet. A dolores quasQui veritatis est aliquid sapiente et enim dolor At harum recusandae qui fugiat aspernatur quo officiis enim? Rem deserunt velit
   <a href="https://www.loremipzum.com" target="_blank">Et officia et delectus libero qui quisquam dolorem</a> qui corporis illo. Et eius blanditiis <em>Sed repudiandae et labore expedita et exercitationem dolores</em> ab cumque omnis est necessitatibus aspernatur eum assumenda eius. </p>
   <ul><li>Sed autem consectetur 33 rerum delectus est molestiae sapiente. </li><li>At suscipit delectus nam nostrum saepe a odio quia et corrupti molestiae. </li><li>Aut sunt deleniti est commodi atque rem ipsa explicabo. </li><li>Est deleniti aspernatur ut galisum dolore eum voluptas accusantium? </li></ul>
 

"""
    with psycopg.connect(os.environ['DATABASE_CONNECTION']) as conn:
        print("TODO Insert data here")

    content += """
<hr><div style="margin:10px 0"><!-- Tag ID: lipsumcom_incontent -->
<div align="center" data-freestar-ad="__336x280 __728x90" id="lipsumcom_incontent" name="lipsumcom_incontent" data-google-query-id="CNT3p6TIwYEDFepfpAQdmEwC3A">
  
<div id="google_ads_iframe_/15184186,22440292294/lipsumcom_incontent_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/15184186,22440292294/lipsumcom_incontent_0" name="google_ads_iframe_/15184186,22440292294/lipsumcom_incontent_0" title="3rd party ad content" width="1" height="1" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Advertisement" tabindex="0" allow="attribution-reporting" style="border: 0px; vertical-align: bottom; width: 728px; height: 90px;" data-load-complete="true" data-google-container-id="6"></iframe><div class="__fs-ancillary" style="--childWidth: 728px; visibility: visible;"><div class="__fs-branding"><a href="https://ads.freestar.com/?utm_campaign=branding&amp;utm_medium=banner&amp;utm_source=lipsum.com&amp;utm_content=lipsumcom_incontent" target="_blank" rel="noreferrer"><img src="https://a.pub.network/core/imgs/fslogo-green.svg" alt="freestar" width="14" height="14"></a></div></div></div></div></div>
<hr><div id="Translation">

<h3>The standard Lorem Ipsum passage, used since the 1500s</h3><p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p><h3>Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC</h3><p>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"</p>
<h3>1914 translation by H. Rackham</h3>
<p>"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"</p>
<h3>Section 1.10.33 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC</h3>
<p>"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."</p>
<h3>1914 translation by H. Rackham</h3>
<p>"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."</p>
</div>
"""

    footer = """
<hr>

<div class="boxed"><a style="text-decoration:none" href="mailto:help@lipsum.com">help@lipsum.com</a><br><a style="text-decoration:none" rel="nofollow" href="/privacy">Privacy Policy</a>
·
<a style="cursor:pointer" class="change-consent" onclick="window.__uspapi('displayUspUi');">Do Not Sell My Personal Information</a>
·
<a style="cursor:pointer" class="change-consent" onclick="window.__tcfapi('displayConsentUi', 2, function() {} );">Change Consent</a>
</div>
</div>
</div>
"""
    return header + content + footer

    
        
if __name__ == "__main__":
    app.run()
