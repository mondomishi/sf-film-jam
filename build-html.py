#!/usr/bin/env python3

from typing import NamedTuple
from datetime import datetime

NEWLINE = "\n"
THIS_YEAR = datetime.now().year


NEXT_JAM_DETAILS = """
<div class="jam-details">
  <h3>NEXT JAM'S DETAILS</h3>
  <ul>
    <li>
      <span>When:&nbsp;</span>
      Sun, Oct 19 from 12-3pm
    </li>
    <li>
      <span>Where:</span>
      Golden Gate Park, SF
    </li>
    <li>
      <span>Theme:</span>
      Will be revealed at the Jam!
    </li>
  </ul>
</div>
"""
PAGE_URL = "https://sffilmjam.com"
PAGE_TITLE = "SF Film Jam"
PAGE_DESCRIPTION = "SF Film Jam. Make a movie in a day. Make mistakes. Make friends."
OG_IMAGE_ALT = "A monkey looking into the eyepiece of a cinema camera."
OG_IMAGE_URL = f"{PAGE_URL}/images/mnkeycam2.jpg"
JOIN_BUTTON_HTML = """
<a class="join-button" target="_blank" rel="noopener noreferrer" href="https://forms.gle/sRabh5kFdnFXgBhH8">
  Get on the list <br /> for future Jams
</a>
"""
HTML_OUT = f"""<!DOCTYPE html>
<html>
  <head>
    <title>{PAGE_TITLE}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta charset="utf-8" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{PAGE_TITLE}" />
    <meta property="og:description" content="{PAGE_DESCRIPTION}" />
    <meta name="description" content="{PAGE_DESCRIPTION}" />
    <meta property="og:url" content="{PAGE_URL}" />
    <link rel="canonical" href="{PAGE_URL}" />
    <meta property="og:site_name" content="{PAGE_TITLE}" />
    <meta property="og:image" content="{OG_IMAGE_URL}" />
    <meta property="og:image:secure_url" content="{OG_IMAGE_URL}" />
    <meta property="og:image:alt" content="{OG_IMAGE_ALT}" />
    <link rel="icon" href="favicon.ico" />
    <link rel="stylesheet" href="normalize.css" />
    <link rel="stylesheet" href="index.css" />
  </head>

  <body><div id="root">
    <header id="header">
      <div id="top-line">
        <img
          id="title-pic"
          alt="{OG_IMAGE_ALT}"
          src="{OG_IMAGE_URL}"
        />
        <div id="titles">
          <h1 id="main-title">{PAGE_TITLE}</h1>
          <div id="subtitles">
            <h2 class="sub-title">make mistakes.</h2>
            <h2 class="sub-title">finish a movie.</h2>
            <h2 class="sub-title">somewhat often.</h2>
          </div>
        </div>
      </div>
    </header>
    <main id="main">
      <div>
        <p>
          Get regular practice working on movies start to finish.
        </p><p>
          Quick. Bad. Done.
        </p>
        <br />
        <p style="font-weight: bold">
          All experience levels welcome!!
        </p>
      </div><div id="details-and-join">
        {NEXT_JAM_DETAILS}
        {JOIN_BUTTON_HTML}
      </div><div class="about-info">
        <h3>HOW IT WORKS</h3>
        <ol>
          <li>
            You tell me:
            <ul style="list-style-type: disc">
              <li>
                <p>what ROLE(s) you're comfortable being assigned</p>
                <p class="mini-p">(screenwriter, actor, director, camera operator, ... etc)</p>
                <p class="mini-p">(all experience levels welcome!!)</p>
              </li>
              <li>
                <p>what GEAR you can bring</p>
                <p class="mini-p">(camera, tripod, lights, ... etc)</p>
                <p class="mini-p">(its ok if you can't bring anything!)</p>
              </li>
            </ul>
          </li>
          <li>
            <p>I match everybody into small crews.</p>
            <p class="mini-p">(each crew is responsible for a movie)</p>
          </li><li>
            <p>We meet up.</p>
            <p class="mini-p">(I handle scheduling)</p>
          </li><li>
            <p>I give out the prompt.</p>
            <p class="mini-p">(and explain the rules)</p>
          </li>
          <li>
            <p style="font-weight: bold">
              We make a (short) movie in one sitting.
            </p><p style="font-weight: bold">
              Full export. No excuses.
            </p>
          </li>
        </ol>
      </div><div class="about-info">
        <p>
          The length of the Jams vary!
        </p>
        <ul>
          <li>
            <p>Some are shorter and force you to rush</p>
            <p class="mini-p">(but require only a small time commitment)</p>
          </li><li>
            <p>Others leave more time to refine your work</p>
            <p class="mini-p">(but require more time commitment)</p>
          </li>
        </ul>
      </div><div class="about-info">
        <div id="my-quote">
          <p style="font-style: italic">
            It's not about making a good movie.
          </p><p style="font-style: italic">
            It's about finishing enough bad movies
          </p><p style="font-style: italic; margin-left: 24px">
            that you eventually start finishing good ones.
          </p>
        </div>
      </div>
      <div id="bottom-join-button-wrapper">{JOIN_BUTTON_HTML}</div>
    </main>
    <footer id="footer">
      <div id="bottom-line">
        <div id="copywrite">© {THIS_YEAR}
        <a target="_blank" rel="noopener noreferrer" href="https://linktr.ee/montelately">Monte Lately</a>.
        All Rights Reserved.</div>
      </div>
    </footer>
  </div></body>
</html>
"""

with open("./docs/index.html", "w") as outFile:
    outFile.write(HTML_OUT)
