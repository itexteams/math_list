import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang16_p4_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang == '1':
                # Khai báo biến
                x = symbols("x")
                y = symbols('y')
                r = randint(3,7)
                xi = 2*r
                xm = randint(2,3)
                ym = randint(2,4)
                while sqrt(xm**2+ym**2)>=r:
                    x = symbols("x")
                    y = symbols('y')
                    r = randint(3,7)
                    xi = 2*r
                    xm = randint(2,3)
                    ym = randint(2,4)

                # Câu hỏi
                noidungcauhoi=(
                    '''Một cái cổng hình bán nguyệt rộng $%s$ cao $%s$ như hình vẽ. mặt đường dưới cổng được chia làm hai làn cho xe ra vào.'''
                            ''' Một chiếc xe tải rộng $%s m$, cao $%s m$ đi đúng làn đường quy định có thể đi qua cổng và không làm hư hỏng cổng hay không?'''
                            '\\begin{center} \n'

                            ''' \\definecolor{qqzzqq}{rgb}{0.,0.6,0.}
            \\definecolor{yqyqyq}{rgb}{0.5019607843137255,0.5019607843137255,0.5019607843137255}
            \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\definecolor{qqccqq}{rgb}{0.,0.8,0.}
            \\definecolor{ffcctt}{rgb}{1.,0.8,0.2}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-0.12247844248433659,-0.14843315652405784) rectangle (6.123275161349983,3.7417790881498796);
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (0.,2.887835066414674) -- (0.9848707994223983,2.8709781278587685) -- (1.001727737978304,1.2864259036036207) -- (0.00716836317985915,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (4.996822175727989,2.8709781278587685) -- (5.982953081248482,2.8709781278587685) -- (5.982953081248482,1.2864259036036207) -- (5.022107583561849,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (0.00716836317985915,1.2864259036036207) -- (1.1871540620932686,1.2864259036036207) -- (0.015596832457812073,0.3087234673610828) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (5.982953081248482,1.2864259036036207) -- (4.8113958516130255,1.2864259036036207) -- (5.9576676734146226,0.33400887519494155) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (0.015596832457812073,0.3087234673610828) -- (2.813848632738183,2.634980988076087) -- (2.878420263580879,2.6428827263047348) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (5.9576676734146226,0.33400887519494155) -- (3.1517932952259757,2.6409225301741723) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- cycle;
                \\fill[line width=1.pt,color=yqyqyq,fill=yqyqyq,fill opacity=1.0] (2.878420263580879,2.6428827263047348) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (2.813848632738183,2.634980988076087) -- (1.9444784253494407,2.634459861112432) -- (1.8812652564056476,2.5677348494495393) -- (1.8075165593045557,2.483450624191149) -- (1.7372797049225632,2.399166398932758) -- (1.667042850540571,2.2832755892024705) -- (1.6003178388776782,2.1498255658766854) -- (1.5406165126529847,2.0023281716745016) -- (1.4984744000237895,1.8267360357195208) -- (1.4738915009900921,1.7073333832701338) -- (1.4715456720996598,1.5190905750151473) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (3.1517932952259757,2.6409225301741723) -- (4.012953786899113,2.637971703831532) -- (4.093726169438405,2.56422300673044) -- (4.192057765573194,2.4553558824383517) -- (4.272830148112486,2.3324413872698653) -- (4.329019631618079,2.2376216338541757) -- (4.395744643280972,2.11119529596659) -- (4.448422284067466,1.9566742163262065) -- (4.487052553977562,1.8337597211577201) -- (4.508123610292159,1.6932860123937354) -- (4.504828864989625,1.5284934578593357) -- cycle;
                \\draw [line width=1.pt,color=ffcctt] (0.,2.887835066414674)-- (0.9848707994223983,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (1.001727737978304,1.2864259036036207)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (0.00716836317985915,1.2864259036036207)-- (0.,2.887835066414674);
                \\draw [line width=1.pt,color=ffcctt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,2.8709781278587685)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,1.2864259036036207)-- (5.022107583561849,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.022107583561849,1.2864259036036207)-- (4.996822175727989,2.8709781278587685);
                \\draw [line width=1.pt,color=qqccqq] (0.00716836317985915,1.2864259036036207)-- (1.1871540620932686,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (1.1871540620932686,1.2864259036036207)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=qqccqq] (0.015596832457812073,0.3087234673610828)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (5.982953081248482,1.2864259036036207)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (4.8113958516130255,1.2864259036036207)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=qqccqq] (5.9576676734146226,0.33400887519494155)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffffff] (0.015596832457812073,0.3087234673610828)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=ffffff] (2.813848632738183,2.634980988076087)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=ffffff] (2.878420263580879,2.6428827263047348)-- (0.,0.);
                \\draw [line width=1.pt,color=ffffff] (0.,0.)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=ffffff] (5.9576676734146226,0.33400887519494155)-- (3.1517932952259757,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.1517932952259757,2.6409225301741723)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=ffffff] (6.,0.)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=yqyqyq] (2.878420263580879,2.6428827263047348)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=yqyqyq] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (6.,0.)-- (0.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (0.,0.)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=qqzzqq] (2.813848632738183,2.634980988076087)-- (1.9444784253494407,2.634459861112432);
                \\draw [line width=1.pt,color=qqzzqq] (1.9444784253494407,2.634459861112432)-- (1.8812652564056476,2.5677348494495393);
                \\draw [line width=1.pt,color=qqzzqq] (1.8812652564056476,2.5677348494495393)-- (1.8075165593045557,2.483450624191149);
                \\draw [line width=1.pt,color=qqzzqq] (1.8075165593045557,2.483450624191149)-- (1.7372797049225632,2.399166398932758);
                \\draw [line width=1.pt,color=qqzzqq] (1.7372797049225632,2.399166398932758)-- (1.667042850540571,2.2832755892024705);
                \\draw [line width=1.pt,color=qqzzqq] (1.667042850540571,2.2832755892024705)-- (1.6003178388776782,2.1498255658766854);
                \\draw [line width=1.pt,color=qqzzqq] (1.6003178388776782,2.1498255658766854)-- (1.5406165126529847,2.0023281716745016);
                \\draw [line width=1.pt,color=qqzzqq] (1.5406165126529847,2.0023281716745016)-- (1.4984744000237895,1.8267360357195208);
                \\draw [line width=1.pt,color=qqzzqq] (1.4984744000237895,1.8267360357195208)-- (1.4738915009900921,1.7073333832701338);
                \\draw [line width=1.pt,color=qqzzqq] (1.4738915009900921,1.7073333832701338)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt,color=qqzzqq] (1.4715456720996598,1.5190905750151473)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=qqzzqq] (3.1517932952259757,2.6409225301741723)-- (4.012953786899113,2.637971703831532);
                \\draw [line width=1.pt,color=qqzzqq] (4.012953786899113,2.637971703831532)-- (4.093726169438405,2.56422300673044);
                \\draw [line width=1.pt,color=qqzzqq] (4.093726169438405,2.56422300673044)-- (4.192057765573194,2.4553558824383517);
                \\draw [line width=1.pt,color=qqzzqq] (4.192057765573194,2.4553558824383517)-- (4.272830148112486,2.3324413872698653);
                \\draw [line width=1.pt,color=qqzzqq] (4.272830148112486,2.3324413872698653)-- (4.329019631618079,2.2376216338541757);
                \\draw [line width=1.pt,color=qqzzqq] (4.329019631618079,2.2376216338541757)-- (4.395744643280972,2.11119529596659);
                \\draw [line width=1.pt,color=qqzzqq] (4.395744643280972,2.11119529596659)-- (4.448422284067466,1.9566742163262065);
                \\draw [line width=1.pt,color=qqzzqq] (4.448422284067466,1.9566742163262065)-- (4.487052553977562,1.8337597211577201);
                \\draw [line width=1.pt,color=qqzzqq] (4.487052553977562,1.8337597211577201)-- (4.508123610292159,1.6932860123937354);
                \\draw [line width=1.pt,color=qqzzqq] (4.508123610292159,1.6932860123937354)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=1.pt,color=qqzzqq] (4.504828864989625,1.5284934578593357)-- (3.1517932952259757,2.6409225301741723);
                \\draw [shift={(2.9992749568531476,1.261412122800319)},line width=1.pt]  plot[domain=0.013802717222278703:3.1277899363675146,variable=\\t]({1.*1.8122935265721776*cos(\\t r)+0.*1.8122935265721776*sin(\\t r)},{0.*1.8122935265721776*cos(\\t r)+1.*1.8122935265721776*sin(\\t r)});
                \\draw [shift={(2.9880854574186206,1.5566353457149886)},line width=1.pt]  plot[domain=-0.018552023393608508:3.1663444625805552,variable=\\t]({1.*1.5170044595393197*cos(\\t r)+0.*1.5170044595393197*sin(\\t r)},{0.*1.5170044595393197*cos(\\t r)+1.*1.5170044595393197*sin(\\t r)});
                \\draw [shift={(2.9908464875751934,-0.874446937115913)},line width=1.pt]  plot[domain=1.0790913042308612:2.062501349358932,variable=\\t]({1.*4.24878186999529*cos(\\t r)+0.*4.24878186999529*sin(\\t r)},{0.*4.24878186999529*cos(\\t r)+1.*4.24878186999529*sin(\\t r)});
                \\draw [shift={(3.005472410949279,-0.655841629816094)},line width=1.pt]  plot[domain=1.0216353252909252:2.117717687577702,variable=\\t]({1.*4.156305868930205*cos(\\t r)+0.*4.156305868930205*sin(\\t r)},{0.*4.156305868930205*cos(\\t r)+1.*4.156305868930205*sin(\\t r)});
                \\draw [line width=1.pt] (1.1871540620932686,1.2864259036036207)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt] (4.8113958516130255,1.2864259036036207)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=2pt,dashed,color=ffffff] (3.,0.)-- (2.9911981847087943,2.6418443945597914);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.021657213614713,1.3146490869575416);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (0.,2.8878350664146737);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (0.007168363179859149,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587703);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (5.982953081248484,1.2864259036036214);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (1.1871540620932686,1.2864259036036207);
                \\draw [<->] (1.3,1.3) -- (4.6,1.3);
                \\draw [<->] (3,1.3) -- (3,3);
                \\draw (2.7,1.3) node[anchor=north west] {$%s m$};
                \\draw (3,2.3) node[anchor=north west] {$%s m$};
            \\end{tikzpicture}'''
            '\\end{center} \n'
                    %(latex(xi), latex(r), latex(xm), latex(ym),latex(2*r), latex(r)))
                # Nội dung lời giải
                loigiai = ('Đặt hệ trục $(Oxy)$ như hình vẽ với gốc $O$ là tâm hình bán nguyệt. \\\\'
                        '\\begin{center} \n'

                            ''' \\definecolor{qqzzqq}{rgb}{0.,0.6,0.}
            \\definecolor{yqyqyq}{rgb}{0.5019607843137255,0.5019607843137255,0.5019607843137255}
            \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\definecolor{qqccqq}{rgb}{0.,0.8,0.}
            \\definecolor{ffcctt}{rgb}{1.,0.8,0.2}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-0.12247844248433659,-0.14843315652405784) rectangle (7,4.5);
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (0.,2.887835066414674) -- (0.9848707994223983,2.8709781278587685) -- (1.001727737978304,1.2864259036036207) -- (0.00716836317985915,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (4.996822175727989,2.8709781278587685) -- (5.982953081248482,2.8709781278587685) -- (5.982953081248482,1.2864259036036207) -- (5.022107583561849,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (0.00716836317985915,1.2864259036036207) -- (1.1871540620932686,1.2864259036036207) -- (0.015596832457812073,0.3087234673610828) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (5.982953081248482,1.2864259036036207) -- (4.8113958516130255,1.2864259036036207) -- (5.9576676734146226,0.33400887519494155) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (0.015596832457812073,0.3087234673610828) -- (2.813848632738183,2.634980988076087) -- (2.878420263580879,2.6428827263047348) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (5.9576676734146226,0.33400887519494155) -- (3.1517932952259757,2.6409225301741723) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- cycle;
                \\fill[line width=1.pt,color=yqyqyq,fill=yqyqyq,fill opacity=1.0] (2.878420263580879,2.6428827263047348) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (2.813848632738183,2.634980988076087) -- (1.9444784253494407,2.634459861112432) -- (1.8812652564056476,2.5677348494495393) -- (1.8075165593045557,2.483450624191149) -- (1.7372797049225632,2.399166398932758) -- (1.667042850540571,2.2832755892024705) -- (1.6003178388776782,2.1498255658766854) -- (1.5406165126529847,2.0023281716745016) -- (1.4984744000237895,1.8267360357195208) -- (1.4738915009900921,1.7073333832701338) -- (1.4715456720996598,1.5190905750151473) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (3.1517932952259757,2.6409225301741723) -- (4.012953786899113,2.637971703831532) -- (4.093726169438405,2.56422300673044) -- (4.192057765573194,2.4553558824383517) -- (4.272830148112486,2.3324413872698653) -- (4.329019631618079,2.2376216338541757) -- (4.395744643280972,2.11119529596659) -- (4.448422284067466,1.9566742163262065) -- (4.487052553977562,1.8337597211577201) -- (4.508123610292159,1.6932860123937354) -- (4.504828864989625,1.5284934578593357) -- cycle;
                \\draw [line width=1.pt,color=ffcctt] (0.,2.887835066414674)-- (0.9848707994223983,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (1.001727737978304,1.2864259036036207)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (0.00716836317985915,1.2864259036036207)-- (0.,2.887835066414674);
                \\draw [line width=1.pt,color=ffcctt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,2.8709781278587685)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,1.2864259036036207)-- (5.022107583561849,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.022107583561849,1.2864259036036207)-- (4.996822175727989,2.8709781278587685);
                \\draw [line width=1.pt,color=qqccqq] (0.00716836317985915,1.2864259036036207)-- (1.1871540620932686,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (1.1871540620932686,1.2864259036036207)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=qqccqq] (0.015596832457812073,0.3087234673610828)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (5.982953081248482,1.2864259036036207)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (4.8113958516130255,1.2864259036036207)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=qqccqq] (5.9576676734146226,0.33400887519494155)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffffff] (0.015596832457812073,0.3087234673610828)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=ffffff] (2.813848632738183,2.634980988076087)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=ffffff] (2.878420263580879,2.6428827263047348)-- (0.,0.);
                \\draw [line width=1.pt,color=ffffff] (0.,0.)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=ffffff] (5.9576676734146226,0.33400887519494155)-- (3.1517932952259757,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.1517932952259757,2.6409225301741723)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=ffffff] (6.,0.)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=yqyqyq] (2.878420263580879,2.6428827263047348)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=yqyqyq] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (6.,0.)-- (0.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (0.,0.)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=qqzzqq] (2.813848632738183,2.634980988076087)-- (1.9444784253494407,2.634459861112432);
                \\draw [line width=1.pt,color=qqzzqq] (1.9444784253494407,2.634459861112432)-- (1.8812652564056476,2.5677348494495393);
                \\draw [line width=1.pt,color=qqzzqq] (1.8812652564056476,2.5677348494495393)-- (1.8075165593045557,2.483450624191149);
                \\draw [line width=1.pt,color=qqzzqq] (1.8075165593045557,2.483450624191149)-- (1.7372797049225632,2.399166398932758);
                \\draw [line width=1.pt,color=qqzzqq] (1.7372797049225632,2.399166398932758)-- (1.667042850540571,2.2832755892024705);
                \\draw [line width=1.pt,color=qqzzqq] (1.667042850540571,2.2832755892024705)-- (1.6003178388776782,2.1498255658766854);
                \\draw [line width=1.pt,color=qqzzqq] (1.6003178388776782,2.1498255658766854)-- (1.5406165126529847,2.0023281716745016);
                \\draw [line width=1.pt,color=qqzzqq] (1.5406165126529847,2.0023281716745016)-- (1.4984744000237895,1.8267360357195208);
                \\draw [line width=1.pt,color=qqzzqq] (1.4984744000237895,1.8267360357195208)-- (1.4738915009900921,1.7073333832701338);
                \\draw [line width=1.pt,color=qqzzqq] (1.4738915009900921,1.7073333832701338)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt,color=qqzzqq] (1.4715456720996598,1.5190905750151473)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=qqzzqq] (3.1517932952259757,2.6409225301741723)-- (4.012953786899113,2.637971703831532);
                \\draw [line width=1.pt,color=qqzzqq] (4.012953786899113,2.637971703831532)-- (4.093726169438405,2.56422300673044);
                \\draw [line width=1.pt,color=qqzzqq] (4.093726169438405,2.56422300673044)-- (4.192057765573194,2.4553558824383517);
                \\draw [line width=1.pt,color=qqzzqq] (4.192057765573194,2.4553558824383517)-- (4.272830148112486,2.3324413872698653);
                \\draw [line width=1.pt,color=qqzzqq] (4.272830148112486,2.3324413872698653)-- (4.329019631618079,2.2376216338541757);
                \\draw [line width=1.pt,color=qqzzqq] (4.329019631618079,2.2376216338541757)-- (4.395744643280972,2.11119529596659);
                \\draw [line width=1.pt,color=qqzzqq] (4.395744643280972,2.11119529596659)-- (4.448422284067466,1.9566742163262065);
                \\draw [line width=1.pt,color=qqzzqq] (4.448422284067466,1.9566742163262065)-- (4.487052553977562,1.8337597211577201);
                \\draw [line width=1.pt,color=qqzzqq] (4.487052553977562,1.8337597211577201)-- (4.508123610292159,1.6932860123937354);
                \\draw [line width=1.pt,color=qqzzqq] (4.508123610292159,1.6932860123937354)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=1.pt,color=qqzzqq] (4.504828864989625,1.5284934578593357)-- (3.1517932952259757,2.6409225301741723);
                \\draw [shift={(2.9992749568531476,1.261412122800319)},line width=1.pt]  plot[domain=0.013802717222278703:3.1277899363675146,variable=\\t]({1.*1.8122935265721776*cos(\\t r)+0.*1.8122935265721776*sin(\\t r)},{0.*1.8122935265721776*cos(\\t r)+1.*1.8122935265721776*sin(\\t r)});
                \\draw [shift={(2.9880854574186206,1.5566353457149886)},line width=1.pt]  plot[domain=-0.018552023393608508:3.1663444625805552,variable=\\t]({1.*1.5170044595393197*cos(\\t r)+0.*1.5170044595393197*sin(\\t r)},{0.*1.5170044595393197*cos(\\t r)+1.*1.5170044595393197*sin(\\t r)});
                \\draw [shift={(2.9908464875751934,-0.874446937115913)},line width=1.pt]  plot[domain=1.0790913042308612:2.062501349358932,variable=\\t]({1.*4.24878186999529*cos(\\t r)+0.*4.24878186999529*sin(\\t r)},{0.*4.24878186999529*cos(\\t r)+1.*4.24878186999529*sin(\\t r)});
                \\draw [shift={(3.005472410949279,-0.655841629816094)},line width=1.pt]  plot[domain=1.0216353252909252:2.117717687577702,variable=\\t]({1.*4.156305868930205*cos(\\t r)+0.*4.156305868930205*sin(\\t r)},{0.*4.156305868930205*cos(\\t r)+1.*4.156305868930205*sin(\\t r)});
                \\draw [line width=1.pt] (1.1871540620932686,1.2864259036036207)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt] (4.8113958516130255,1.2864259036036207)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=2pt,dashed,color=ffffff] (3.,0.)-- (2.9911981847087943,2.6418443945597914);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.021657213614713,1.3146490869575416);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (0.,2.8878350664146737);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (0.007168363179859149,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587703);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (5.982953081248484,1.2864259036036214);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (1.1871540620932686,1.2864259036036207);
                \\draw [->] (3,1.3) -- (6.8,1.3);
                \\draw [->] (3,1.3) -- (3,4.2);
                \\draw (3.6,1.3) node[anchor=north west] {$%s m$};
                \\draw (3,2.3) node[anchor=north west] {$%s m$};
                \\draw (2.5,1.6) node[anchor=north west] {$O$};
                \\draw (6.5,1.3) node[anchor=north west] {$x$};
                \\draw (2.4,4.2) node[anchor=north west] {$y$};
            \\end{tikzpicture}'''
            '\\end{center} \n'
                        ' Khi đó cái cổng được cho bởi nửa đường tròn tâm $O$, bán kính $R=%s m$; phương trình nửa đường tròn là $\\heva {& x^2+y^2=%s^2\\\\ & y\\ge 0}$.\\\\ \n'
                        ' Xe tải đi ở làn bên phải (ứng với một phần tư đường tròn bên phải). Xe tải muốn đi qua không vướng gì thì đường chéo mặt cắt ngang của xe tải (giả sử là hình chữ nhật) nhỏ hơn bán kính cổng bán nguyệt.\\\\ \n'
                        ' Đường chéo cần tìm là $\\sqrt{%s^2+%s^2}= %s <R$.\\\\ \n'
                        'Vậy chiếc xe tải như trên có thể qua cổng mà không gây hư hỏng gì.'

                        %(latex(r),latex(r),latex(r),latex(r),latex(xm),latex(ym),latex(sqrt(xm**2+ym**2)),)
                                    )

            if dang == '2':
                # Khai báo biến
                x = symbols("x")
                y = symbols('y')
                r = randint(3,7)
                xi = 2*r
                xm = randint(2,3)
                ym = randint(2,4)
                while sqrt(xm**2+ym**2)<=r:
                    x = symbols("x")
                    y = symbols('y')
                    r = randint(3,7)
                    xi = 2*r
                    xm = randint(2,3)
                    ym = randint(2,4)




                # Câu hỏi
                noidungcauhoi=(
                    '''Một cái cổng hình bán nguyệt rộng $%s$ cao $%s$ như hình vẽ. mặt đường dưới cổng được chia làm hai làn cho xe ra vào.'''
                            ''' Một chiếc xe tải rộng $%s m$, cao $%s m$ đi đúng làn đường quy định có thể đi qua cổng và không làm hư hỏng cổng hay không?'''
                            '\\begin{center} \n'

                            ''' \\definecolor{qqzzqq}{rgb}{0.,0.6,0.}
            \\definecolor{yqyqyq}{rgb}{0.5019607843137255,0.5019607843137255,0.5019607843137255}
            \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\definecolor{qqccqq}{rgb}{0.,0.8,0.}
            \\definecolor{ffcctt}{rgb}{1.,0.8,0.2}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-0.12247844248433659,-0.14843315652405784) rectangle (6.123275161349983,3.7417790881498796);
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (0.,2.887835066414674) -- (0.9848707994223983,2.8709781278587685) -- (1.001727737978304,1.2864259036036207) -- (0.00716836317985915,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (4.996822175727989,2.8709781278587685) -- (5.982953081248482,2.8709781278587685) -- (5.982953081248482,1.2864259036036207) -- (5.022107583561849,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (0.00716836317985915,1.2864259036036207) -- (1.1871540620932686,1.2864259036036207) -- (0.015596832457812073,0.3087234673610828) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (5.982953081248482,1.2864259036036207) -- (4.8113958516130255,1.2864259036036207) -- (5.9576676734146226,0.33400887519494155) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (0.015596832457812073,0.3087234673610828) -- (2.813848632738183,2.634980988076087) -- (2.878420263580879,2.6428827263047348) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (5.9576676734146226,0.33400887519494155) -- (3.1517932952259757,2.6409225301741723) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- cycle;
                \\fill[line width=1.pt,color=yqyqyq,fill=yqyqyq,fill opacity=1.0] (2.878420263580879,2.6428827263047348) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (2.813848632738183,2.634980988076087) -- (1.9444784253494407,2.634459861112432) -- (1.8812652564056476,2.5677348494495393) -- (1.8075165593045557,2.483450624191149) -- (1.7372797049225632,2.399166398932758) -- (1.667042850540571,2.2832755892024705) -- (1.6003178388776782,2.1498255658766854) -- (1.5406165126529847,2.0023281716745016) -- (1.4984744000237895,1.8267360357195208) -- (1.4738915009900921,1.7073333832701338) -- (1.4715456720996598,1.5190905750151473) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (3.1517932952259757,2.6409225301741723) -- (4.012953786899113,2.637971703831532) -- (4.093726169438405,2.56422300673044) -- (4.192057765573194,2.4553558824383517) -- (4.272830148112486,2.3324413872698653) -- (4.329019631618079,2.2376216338541757) -- (4.395744643280972,2.11119529596659) -- (4.448422284067466,1.9566742163262065) -- (4.487052553977562,1.8337597211577201) -- (4.508123610292159,1.6932860123937354) -- (4.504828864989625,1.5284934578593357) -- cycle;
                \\draw [line width=1.pt,color=ffcctt] (0.,2.887835066414674)-- (0.9848707994223983,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (1.001727737978304,1.2864259036036207)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (0.00716836317985915,1.2864259036036207)-- (0.,2.887835066414674);
                \\draw [line width=1.pt,color=ffcctt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,2.8709781278587685)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,1.2864259036036207)-- (5.022107583561849,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.022107583561849,1.2864259036036207)-- (4.996822175727989,2.8709781278587685);
                \\draw [line width=1.pt,color=qqccqq] (0.00716836317985915,1.2864259036036207)-- (1.1871540620932686,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (1.1871540620932686,1.2864259036036207)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=qqccqq] (0.015596832457812073,0.3087234673610828)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (5.982953081248482,1.2864259036036207)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (4.8113958516130255,1.2864259036036207)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=qqccqq] (5.9576676734146226,0.33400887519494155)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffffff] (0.015596832457812073,0.3087234673610828)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=ffffff] (2.813848632738183,2.634980988076087)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=ffffff] (2.878420263580879,2.6428827263047348)-- (0.,0.);
                \\draw [line width=1.pt,color=ffffff] (0.,0.)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=ffffff] (5.9576676734146226,0.33400887519494155)-- (3.1517932952259757,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.1517932952259757,2.6409225301741723)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=ffffff] (6.,0.)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=yqyqyq] (2.878420263580879,2.6428827263047348)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=yqyqyq] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (6.,0.)-- (0.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (0.,0.)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=qqzzqq] (2.813848632738183,2.634980988076087)-- (1.9444784253494407,2.634459861112432);
                \\draw [line width=1.pt,color=qqzzqq] (1.9444784253494407,2.634459861112432)-- (1.8812652564056476,2.5677348494495393);
                \\draw [line width=1.pt,color=qqzzqq] (1.8812652564056476,2.5677348494495393)-- (1.8075165593045557,2.483450624191149);
                \\draw [line width=1.pt,color=qqzzqq] (1.8075165593045557,2.483450624191149)-- (1.7372797049225632,2.399166398932758);
                \\draw [line width=1.pt,color=qqzzqq] (1.7372797049225632,2.399166398932758)-- (1.667042850540571,2.2832755892024705);
                \\draw [line width=1.pt,color=qqzzqq] (1.667042850540571,2.2832755892024705)-- (1.6003178388776782,2.1498255658766854);
                \\draw [line width=1.pt,color=qqzzqq] (1.6003178388776782,2.1498255658766854)-- (1.5406165126529847,2.0023281716745016);
                \\draw [line width=1.pt,color=qqzzqq] (1.5406165126529847,2.0023281716745016)-- (1.4984744000237895,1.8267360357195208);
                \\draw [line width=1.pt,color=qqzzqq] (1.4984744000237895,1.8267360357195208)-- (1.4738915009900921,1.7073333832701338);
                \\draw [line width=1.pt,color=qqzzqq] (1.4738915009900921,1.7073333832701338)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt,color=qqzzqq] (1.4715456720996598,1.5190905750151473)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=qqzzqq] (3.1517932952259757,2.6409225301741723)-- (4.012953786899113,2.637971703831532);
                \\draw [line width=1.pt,color=qqzzqq] (4.012953786899113,2.637971703831532)-- (4.093726169438405,2.56422300673044);
                \\draw [line width=1.pt,color=qqzzqq] (4.093726169438405,2.56422300673044)-- (4.192057765573194,2.4553558824383517);
                \\draw [line width=1.pt,color=qqzzqq] (4.192057765573194,2.4553558824383517)-- (4.272830148112486,2.3324413872698653);
                \\draw [line width=1.pt,color=qqzzqq] (4.272830148112486,2.3324413872698653)-- (4.329019631618079,2.2376216338541757);
                \\draw [line width=1.pt,color=qqzzqq] (4.329019631618079,2.2376216338541757)-- (4.395744643280972,2.11119529596659);
                \\draw [line width=1.pt,color=qqzzqq] (4.395744643280972,2.11119529596659)-- (4.448422284067466,1.9566742163262065);
                \\draw [line width=1.pt,color=qqzzqq] (4.448422284067466,1.9566742163262065)-- (4.487052553977562,1.8337597211577201);
                \\draw [line width=1.pt,color=qqzzqq] (4.487052553977562,1.8337597211577201)-- (4.508123610292159,1.6932860123937354);
                \\draw [line width=1.pt,color=qqzzqq] (4.508123610292159,1.6932860123937354)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=1.pt,color=qqzzqq] (4.504828864989625,1.5284934578593357)-- (3.1517932952259757,2.6409225301741723);
                \\draw [shift={(2.9992749568531476,1.261412122800319)},line width=1.pt]  plot[domain=0.013802717222278703:3.1277899363675146,variable=\\t]({1.*1.8122935265721776*cos(\\t r)+0.*1.8122935265721776*sin(\\t r)},{0.*1.8122935265721776*cos(\\t r)+1.*1.8122935265721776*sin(\\t r)});
                \\draw [shift={(2.9880854574186206,1.5566353457149886)},line width=1.pt]  plot[domain=-0.018552023393608508:3.1663444625805552,variable=\\t]({1.*1.5170044595393197*cos(\\t r)+0.*1.5170044595393197*sin(\\t r)},{0.*1.5170044595393197*cos(\\t r)+1.*1.5170044595393197*sin(\\t r)});
                \\draw [shift={(2.9908464875751934,-0.874446937115913)},line width=1.pt]  plot[domain=1.0790913042308612:2.062501349358932,variable=\\t]({1.*4.24878186999529*cos(\\t r)+0.*4.24878186999529*sin(\\t r)},{0.*4.24878186999529*cos(\\t r)+1.*4.24878186999529*sin(\\t r)});
                \\draw [shift={(3.005472410949279,-0.655841629816094)},line width=1.pt]  plot[domain=1.0216353252909252:2.117717687577702,variable=\\t]({1.*4.156305868930205*cos(\\t r)+0.*4.156305868930205*sin(\\t r)},{0.*4.156305868930205*cos(\\t r)+1.*4.156305868930205*sin(\\t r)});
                \\draw [line width=1.pt] (1.1871540620932686,1.2864259036036207)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt] (4.8113958516130255,1.2864259036036207)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=2pt,dashed,color=ffffff] (3.,0.)-- (2.9911981847087943,2.6418443945597914);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.021657213614713,1.3146490869575416);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (0.,2.8878350664146737);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (0.007168363179859149,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587703);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (5.982953081248484,1.2864259036036214);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (1.1871540620932686,1.2864259036036207);
                \\draw [<->] (1.3,1.3) -- (4.6,1.3);
                \\draw [<->] (3,1.3) -- (3,3);
                \\draw (2.7,1.3) node[anchor=north west] {$%s m$};
                \\draw (3,2.3) node[anchor=north west] {$%s m$};
            \\end{tikzpicture}'''
            '\\end{center} \n'
                    %(latex(xi), latex(r), latex(xm), latex(ym),latex(2*r), latex(r)))
                # Nội dung lời giải
                loigiai = ('Đặt hệ trục $(Oxy)$ như hình vẽ với gốc $O$ là tâm hình bán nguyệt. \\\\'
                        '\\begin{center} \n'

                            ''' \\definecolor{qqzzqq}{rgb}{0.,0.6,0.}
            \\definecolor{yqyqyq}{rgb}{0.5019607843137255,0.5019607843137255,0.5019607843137255}
            \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\definecolor{qqccqq}{rgb}{0.,0.8,0.}
            \\definecolor{ffcctt}{rgb}{1.,0.8,0.2}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-0.12247844248433659,-0.14843315652405784) rectangle (7,4.5);
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (0.,2.887835066414674) -- (0.9848707994223983,2.8709781278587685) -- (1.001727737978304,1.2864259036036207) -- (0.00716836317985915,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=ffcctt,fill=ffcctt,fill opacity=1.0] (4.996822175727989,2.8709781278587685) -- (5.982953081248482,2.8709781278587685) -- (5.982953081248482,1.2864259036036207) -- (5.022107583561849,1.2864259036036207) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (0.00716836317985915,1.2864259036036207) -- (1.1871540620932686,1.2864259036036207) -- (0.015596832457812073,0.3087234673610828) -- cycle;
                \\fill[line width=1.pt,color=qqccqq,fill=qqccqq,fill opacity=1.0] (5.982953081248482,1.2864259036036207) -- (4.8113958516130255,1.2864259036036207) -- (5.9576676734146226,0.33400887519494155) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (0.015596832457812073,0.3087234673610828) -- (2.813848632738183,2.634980988076087) -- (2.878420263580879,2.6428827263047348) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=ffffff,fill=ffffff,fill opacity=1.0] (5.9576676734146226,0.33400887519494155) -- (3.1517932952259757,2.6409225301741723) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- cycle;
                \\fill[line width=1.pt,color=yqyqyq,fill=yqyqyq,fill opacity=1.0] (2.878420263580879,2.6428827263047348) -- (3.0913260575958894,2.6409225301741723) -- (6.,0.) -- (0.,0.) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (2.813848632738183,2.634980988076087) -- (1.9444784253494407,2.634459861112432) -- (1.8812652564056476,2.5677348494495393) -- (1.8075165593045557,2.483450624191149) -- (1.7372797049225632,2.399166398932758) -- (1.667042850540571,2.2832755892024705) -- (1.6003178388776782,2.1498255658766854) -- (1.5406165126529847,2.0023281716745016) -- (1.4984744000237895,1.8267360357195208) -- (1.4738915009900921,1.7073333832701338) -- (1.4715456720996598,1.5190905750151473) -- cycle;
                \\fill[line width=1.pt,color=qqzzqq,fill=qqzzqq,fill opacity=1.0] (3.1517932952259757,2.6409225301741723) -- (4.012953786899113,2.637971703831532) -- (4.093726169438405,2.56422300673044) -- (4.192057765573194,2.4553558824383517) -- (4.272830148112486,2.3324413872698653) -- (4.329019631618079,2.2376216338541757) -- (4.395744643280972,2.11119529596659) -- (4.448422284067466,1.9566742163262065) -- (4.487052553977562,1.8337597211577201) -- (4.508123610292159,1.6932860123937354) -- (4.504828864989625,1.5284934578593357) -- cycle;
                \\draw [line width=1.pt,color=ffcctt] (0.,2.887835066414674)-- (0.9848707994223983,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (1.001727737978304,1.2864259036036207)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (0.00716836317985915,1.2864259036036207)-- (0.,2.887835066414674);
                \\draw [line width=1.pt,color=ffcctt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587685);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,2.8709781278587685)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.982953081248482,1.2864259036036207)-- (5.022107583561849,1.2864259036036207);
                \\draw [line width=1.pt,color=ffcctt] (5.022107583561849,1.2864259036036207)-- (4.996822175727989,2.8709781278587685);
                \\draw [line width=1.pt,color=qqccqq] (0.00716836317985915,1.2864259036036207)-- (1.1871540620932686,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (1.1871540620932686,1.2864259036036207)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=qqccqq] (0.015596832457812073,0.3087234673610828)-- (0.00716836317985915,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (5.982953081248482,1.2864259036036207)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt,color=qqccqq] (4.8113958516130255,1.2864259036036207)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=qqccqq] (5.9576676734146226,0.33400887519494155)-- (5.982953081248482,1.2864259036036207);
                \\draw [line width=1.pt,color=ffffff] (0.015596832457812073,0.3087234673610828)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=ffffff] (2.813848632738183,2.634980988076087)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=ffffff] (2.878420263580879,2.6428827263047348)-- (0.,0.);
                \\draw [line width=1.pt,color=ffffff] (0.,0.)-- (0.015596832457812073,0.3087234673610828);
                \\draw [line width=1.pt,color=ffffff] (5.9576676734146226,0.33400887519494155)-- (3.1517932952259757,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.1517932952259757,2.6409225301741723)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=ffffff] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=ffffff] (6.,0.)-- (5.9576676734146226,0.33400887519494155);
                \\draw [line width=1.pt,color=yqyqyq] (2.878420263580879,2.6428827263047348)-- (3.0913260575958894,2.6409225301741723);
                \\draw [line width=1.pt,color=yqyqyq] (3.0913260575958894,2.6409225301741723)-- (6.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (6.,0.)-- (0.,0.);
                \\draw [line width=1.pt,color=yqyqyq] (0.,0.)-- (2.878420263580879,2.6428827263047348);
                \\draw [line width=1.pt,color=qqzzqq] (2.813848632738183,2.634980988076087)-- (1.9444784253494407,2.634459861112432);
                \\draw [line width=1.pt,color=qqzzqq] (1.9444784253494407,2.634459861112432)-- (1.8812652564056476,2.5677348494495393);
                \\draw [line width=1.pt,color=qqzzqq] (1.8812652564056476,2.5677348494495393)-- (1.8075165593045557,2.483450624191149);
                \\draw [line width=1.pt,color=qqzzqq] (1.8075165593045557,2.483450624191149)-- (1.7372797049225632,2.399166398932758);
                \\draw [line width=1.pt,color=qqzzqq] (1.7372797049225632,2.399166398932758)-- (1.667042850540571,2.2832755892024705);
                \\draw [line width=1.pt,color=qqzzqq] (1.667042850540571,2.2832755892024705)-- (1.6003178388776782,2.1498255658766854);
                \\draw [line width=1.pt,color=qqzzqq] (1.6003178388776782,2.1498255658766854)-- (1.5406165126529847,2.0023281716745016);
                \\draw [line width=1.pt,color=qqzzqq] (1.5406165126529847,2.0023281716745016)-- (1.4984744000237895,1.8267360357195208);
                \\draw [line width=1.pt,color=qqzzqq] (1.4984744000237895,1.8267360357195208)-- (1.4738915009900921,1.7073333832701338);
                \\draw [line width=1.pt,color=qqzzqq] (1.4738915009900921,1.7073333832701338)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt,color=qqzzqq] (1.4715456720996598,1.5190905750151473)-- (2.813848632738183,2.634980988076087);
                \\draw [line width=1.pt,color=qqzzqq] (3.1517932952259757,2.6409225301741723)-- (4.012953786899113,2.637971703831532);
                \\draw [line width=1.pt,color=qqzzqq] (4.012953786899113,2.637971703831532)-- (4.093726169438405,2.56422300673044);
                \\draw [line width=1.pt,color=qqzzqq] (4.093726169438405,2.56422300673044)-- (4.192057765573194,2.4553558824383517);
                \\draw [line width=1.pt,color=qqzzqq] (4.192057765573194,2.4553558824383517)-- (4.272830148112486,2.3324413872698653);
                \\draw [line width=1.pt,color=qqzzqq] (4.272830148112486,2.3324413872698653)-- (4.329019631618079,2.2376216338541757);
                \\draw [line width=1.pt,color=qqzzqq] (4.329019631618079,2.2376216338541757)-- (4.395744643280972,2.11119529596659);
                \\draw [line width=1.pt,color=qqzzqq] (4.395744643280972,2.11119529596659)-- (4.448422284067466,1.9566742163262065);
                \\draw [line width=1.pt,color=qqzzqq] (4.448422284067466,1.9566742163262065)-- (4.487052553977562,1.8337597211577201);
                \\draw [line width=1.pt,color=qqzzqq] (4.487052553977562,1.8337597211577201)-- (4.508123610292159,1.6932860123937354);
                \\draw [line width=1.pt,color=qqzzqq] (4.508123610292159,1.6932860123937354)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=1.pt,color=qqzzqq] (4.504828864989625,1.5284934578593357)-- (3.1517932952259757,2.6409225301741723);
                \\draw [shift={(2.9992749568531476,1.261412122800319)},line width=1.pt]  plot[domain=0.013802717222278703:3.1277899363675146,variable=\\t]({1.*1.8122935265721776*cos(\\t r)+0.*1.8122935265721776*sin(\\t r)},{0.*1.8122935265721776*cos(\\t r)+1.*1.8122935265721776*sin(\\t r)});
                \\draw [shift={(2.9880854574186206,1.5566353457149886)},line width=1.pt]  plot[domain=-0.018552023393608508:3.1663444625805552,variable=\\t]({1.*1.5170044595393197*cos(\\t r)+0.*1.5170044595393197*sin(\\t r)},{0.*1.5170044595393197*cos(\\t r)+1.*1.5170044595393197*sin(\\t r)});
                \\draw [shift={(2.9908464875751934,-0.874446937115913)},line width=1.pt]  plot[domain=1.0790913042308612:2.062501349358932,variable=\\t]({1.*4.24878186999529*cos(\\t r)+0.*4.24878186999529*sin(\\t r)},{0.*4.24878186999529*cos(\\t r)+1.*4.24878186999529*sin(\\t r)});
                \\draw [shift={(3.005472410949279,-0.655841629816094)},line width=1.pt]  plot[domain=1.0216353252909252:2.117717687577702,variable=\\t]({1.*4.156305868930205*cos(\\t r)+0.*4.156305868930205*sin(\\t r)},{0.*4.156305868930205*cos(\\t r)+1.*4.156305868930205*sin(\\t r)});
                \\draw [line width=1.pt] (1.1871540620932686,1.2864259036036207)-- (1.4715456720996598,1.5190905750151473);
                \\draw [line width=1.pt] (4.8113958516130255,1.2864259036036207)-- (4.504828864989625,1.5284934578593357);
                \\draw [line width=2pt,dashed,color=ffffff] (3.,0.)-- (2.9911981847087943,2.6418443945597914);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (1.001727737978304,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.021657213614713,1.3146490869575416);
                \\draw [line width=1.pt] (0.9848707994223983,2.8709781278587685)-- (0.,2.8878350664146737);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (0.007168363179859149,1.2864259036036205);
                \\draw [line width=1.pt] (4.996822175727989,2.8709781278587685)-- (5.982953081248482,2.8709781278587703);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (5.982953081248484,1.2864259036036214);
                \\draw [line width=1.pt] (5.021657213614713,1.3146490869575416)-- (4.8113958516130255,1.2864259036036207);
                \\draw [line width=1.pt] (1.001727737978304,1.2864259036036205)-- (1.1871540620932686,1.2864259036036207);
                \\draw [->] (3,1.3) -- (6.8,1.3);
                \\draw [->] (3,1.3) -- (3,4.2);
                \\draw (3.6,1.3) node[anchor=north west] {$%s m$};
                \\draw (3,2.3) node[anchor=north west] {$%s m$};
                \\draw (2.5,1.6) node[anchor=north west] {$O$};
                \\draw (6.5,1.3) node[anchor=north west] {$x$};
                \\draw (2.4,4.2) node[anchor=north west] {$y$};
            \\end{tikzpicture}'''
            '\\end{center} \n'
                        ' Khi đó cái cổng được cho bởi nửa đường tròn tâm $O$, bán kính $R=%s m$; phương trình nửa đường tròn là $\\heva {& x^2+y^2=%s^2\\\\ & y\\ge 0}$.\\\\ \n'
                        ' Xe tải đi ở làn bên phải (ứng với một phần tư đường tròn bên phải). Xe tải muốn đi qua không vướng gì thì đường chéo mặt cắt ngang của xe tải (giả sử là hình chữ nhật) nhỏ hơn bán kính cổng bán nguyệt.\\\\ \n'
                        ' Đường chéo cần tìm là $\\sqrt{%s^2+%s^2}= %s >R$.\\\\ \n'
                        'Vậy chiếc xe tải như trên không thể qua cổng mà không gây hư hỏng gì.'

                        %(latex(r),latex(r),latex(r),latex(r),latex(xm),latex(ym),latex(sqrt(xm**2+ym**2)),)
                                    )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

