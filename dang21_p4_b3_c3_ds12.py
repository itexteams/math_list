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


def bt_dang21_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                d1=randint(15,25)
                d2=d1+1
                c1=-d1/2
                c2=d1/2
                c3=-d2/2
                c4=d2/2
                h1=randint(20,25)
                h2=h1/10
                h3=h2+0.5
                s=randint(3,6)
                v=nsimplify((2/3)*s*(d2*h3-d1*h2))
                while d1==17 or h3==2.7 or d1==20 or h2==2.1 or h2 ==2.3 or d1==23 or h2==2.4:
                    d1=randint(15,25)
                    d2=d1+1
                    c1=-d1/2
                    c2=d1/2
                    c3=-d2/2
                    c4=d2/2
                    h1=randint(20,25)
                    h2=h1/10
                    h3=h2+0.5
                    s=randint(3,6)
                    v=nsimplify((2/3)*s*(d2*h3-d1*h2))
                number = Decimal(float(v))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                if (v)==int(v):
                    kqq='=%s'%(latex(v))
                    db=''
                    qk='%s'%(latex(v))
                else:
                    kqq='\\approx %s'%(latex(kq))
                    db='(kết quả làm tròn đến hàng phần chục của đơn vị mét khối).'
                    qk='%s'%(latex(kq))

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Trong chương trình nông thôn mới, tại một xã X có xây một cây cầu bằng bê tông như hình vẽ, đường cong trong hình vẽ là các đường parabol. Tính thể tích khối bê tông để đổ đủ cây cầu? %s'
                                '}{'
                                '\\scalebox{0.9}{ '  
                            ' \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                '\\clip(-6,-2) rectangle (2.0944881919987632,2.2246946095801112);\n'
                '\\draw [shift={(-0.03195144171888269,0.7866741625143341)},line width=0.8pt]  plot[domain=0.7854670850902558:2.383690798893705,variable=\\t]({1.*0.9426350491286731*cos(\\t r)+0.*0.9426350491286731*sin(\\t r)},{0.*0.9426350491286731*cos(\\t r)+1.*0.9426350491286731*sin(\\t r)});\n'
                '\\draw [shift={(-1.438935806580184,-0.9138932268110337)},line width=0.8pt]  plot[domain=0.2970259939202828:0.8514354790206218,variable=\\t]({1.*3.1468650965072453*cos(\\t r)+0.*3.1468650965072453*sin(\\t r)},{0.*3.1468650965072453*cos(\\t r)+1.*3.1468650965072453*sin(\\t r)});\n'
                '\\draw [shift={(1.4246807202857596,-0.7778571761976381)},line width=0.8pt,dashed]  plot[domain=2.3398310085661786:2.8808423545124757,variable=\\t]({1.*3.078976141375616*cos(\\t r)+0.*3.078976141375616*sin(\\t r)},{0.*3.078976141375616*cos(\\t r)+1.*3.078976141375616*sin(\\t r)});\n'
                '\\draw [shift={(0.0015065977442966637,0.23556291445715552)},line width=0.8pt,dashed]  plot[domain=0.7433374534911091:2.3042803758851607,variable=\\t]({1.*0.6099580128209037*cos(\\t r)+0.*0.6099580128209037*sin(\\t r)},{0.*0.6099580128209037*cos(\\t r)+1.*0.6099580128209037*sin(\\t r)});\n'
                '\\draw [shift={(-1.2522529783658614,-0.8147320490019483)},line width=0.8pt,dashed]  plot[domain=0.37478916906229404:0.70981804643234,variable=\\t]({1.*2.2450403229328937*cos(\\t r)+0.*2.2450403229328937*sin(\\t r)},{0.*2.2450403229328937*cos(\\t r)+1.*2.2450403229328937*sin(\\t r)});\n'
                '\\draw [shift={(0.8126679481418305,-0.4627640910175891)},line width=0.8pt,dashed]  plot[domain=2.3848979427362647:2.8450001420141278,variable=\\t]({1.*1.6771965723745104*cos(\\t r)+0.*1.6771965723745104*sin(\\t r)},{0.*1.6771965723745104*cos(\\t r)+1.*1.6771965723745104*sin(\\t r)});\n'
                '\\draw [shift={(-4.074652796257185,-0.7097307251546232)},line width=0.8pt]  plot[domain=0.7445947433065315:2.3331877593376293,variable=\\t]({1.*0.9241196641511031*cos(\\t r)+0.*0.9241196641511031*sin(\\t r)},{0.*0.9241196641511031*cos(\\t r)+1.*0.9241196641511031*sin(\\t r)});\n'
                '\\draw [shift={(-7.082244406990693,-3.386964441940012)},line width=0.8pt]  plot[domain=0.39063360069159375:0.7305698993864708,variable=\\t]({1.*4.950568200629588*cos(\\t r)+0.*4.950568200629588*sin(\\t r)},{0.*4.950568200629588*cos(\\t r)+1.*4.950568200629588*sin(\\t r)});\n'
                '\\draw [shift={(-1.969414574987402,-2.607982693000769)},line width=0.8pt]  plot[domain=2.38950039701176:2.8459522154407684,variable=\\t]({1.*3.7568536784958084*cos(\\t r)+0.*3.7568536784958084*sin(\\t r)},{0.*3.7568536784958084*cos(\\t r)+1.*3.7568536784958084*sin(\\t r)});\n'
                '\\draw [shift={(-4.113369602511252,-1.301401795357917)},line width=0.8pt]  plot[domain=0.7776739670023851:2.299076550356551,variable=\\t]({1.*0.5856078057002974*cos(\\t r)+0.*0.5856078057002974*sin(\\t r)},{0.*0.5856078057002974*cos(\\t r)+1.*0.5856078057002974*sin(\\t r)});\n'
                '\\draw [shift={(-5.739270339345064,-3.0961770444592362)},line width=0.8pt]  plot[domain=0.5544020096943403:0.8236201267962598,variable=\\t]({1.*3.006569431137379*cos(\\t r)+0.*3.006569431137379*sin(\\t r)},{0.*3.006569431137379*cos(\\t r)+1.*3.006569431137379*sin(\\t r)});\n'
                '\\draw [shift={(-2.464008025923585,-2.6945363044504838)},line width=0.8pt]  plot[domain=2.410143609678028:2.6912635573829746,variable=\\t]({1.*2.7400088596928915*cos(\\t r)+0.*2.7400088596928915*sin(\\t r)},{0.*2.7400088596928915*cos(\\t r)+1.*2.7400088596928915*sin(\\t r)});\n'
                '\\draw [line width=0.8pt,dashed] (-1.550216232788688,0.015919995147472624)-- (-0.7912987377928602,0.027418745071651825);\n'
                '\\draw [line width=0.8pt] (-5.563279956327232,-1.5134137447683609)-- (-4.930848710497376,-1.5019149948441817);\n'
                '\\draw [line width=0.8pt] (-3.1830387220221357,-1.5134137447683609)-- (-2.5046124764955624,-1.5019149948441817);\n'
                '\\draw [line width=0.8pt] (-4.14893371565319,0.211398743858519)-- (-0.04387999272121152,1.7292337338501733);\n'
                '\\draw [line width=0.8pt,dashed] (-4.14893371565319,0.211398743858519)-- (-4.13743496572901,-1.5019149948441817);\n'
                '\\draw [line width=0.8pt,dashed] (-3.1830387220221357,-1.5134137447683609)-- (0.8369474727567111,0.00712409815755994);\n'
                '\\draw [line width=0.8pt] (-2.5046124764955624,-1.5019149948441817)-- (1.5701316607131717,0.00712409815755994);\n'
                '\\draw [line width=0.8pt,dashed] (-5.563279956327232,-1.5134137447683609)-- (-1.550216232788688,0.015919995147472624);\n'
                '\\draw [line width=0.8pt,dashed] (-4.930848710497376,-1.5019149948441817)-- (-0.7912987377928602,0.027418745071651825);\n'
                '\\draw [line width=0.8pt,dashed] (-4.183429965425727,-0.72)-- (-0.04387999272121152,0.843829989688375);\n'
                '\\draw [line width=1.pt ,dashed] (-0.7912987377928602,0.027418745071651825) -- (1.5,0.);\n'
                '\\draw [line width=1.pt ,dashed] (1.9296147115754891E-4,0.019643973838957246) -- (0.013613756899684528,1.75);\n'
                '\\draw (-0.720062460742486,1.4501179994251638) node[anchor=north west] {$0,5\\text{m}$};\n'
                '\\draw (-0.48999020030042206,0.6755413892702163) node[anchor=north west] {$%s\\text{m}$};\n'
                '\\draw (-0.32127054264290844,-0.5975251185092022) node[anchor=north west] {$%s\\text{m}$};\n'
                '\\draw (-3.1895047228206397,-1.4948069342332502) node[anchor=north west] {$0,5\\text{m}$};\n'
                '\\draw (-5.651277909550724,-1.4948069342332502) node[anchor=north west] {$0,5\\text{m}$};\n'
                '\\draw (-4.493247531992336,-1.4487924821448375) node[anchor=north west] {$%s\\text{m}$};\n'
                '\\draw [line width=0.8pt,dashed] (-4.930848710497376,-1.5019149948441817)-- (-3.1830387220221357,-1.5134137447683609);\n'
                                '\\end{tikzpicture}}}\n'
                                %(db,latex(h2),latex(s),latex(d1))
                                )

                # Nội dung lời giải
                loigiai = ('Chọn hệ trục tọa độ $(Oxy)$ như hình vẽ'
                        '\\begin{center}\n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                        '\\clip(-6,-2) rectangle (2.0944881919987632,2.2246946095801112);\n'
                        '\\draw [shift={(-0.03195144171888269,0.7866741625143341)},line width=0.8pt]  plot[domain=0.7854670850902558:2.383690798893705,variable=\\t]({1.*0.9426350491286731*cos(\\t r)+0.*0.9426350491286731*sin(\\t r)},{0.*0.9426350491286731*cos(\\t r)+1.*0.9426350491286731*sin(\\t r)});\n'
                        '\\draw [shift={(-1.438935806580184,-0.9138932268110337)},line width=0.8pt]  plot[domain=0.2970259939202828:0.8514354790206218,variable=\\t]({1.*3.1468650965072453*cos(\\t r)+0.*3.1468650965072453*sin(\\t r)},{0.*3.1468650965072453*cos(\\t r)+1.*3.1468650965072453*sin(\\t r)});\n'
                        '\\draw [shift={(1.4246807202857596,-0.7778571761976381)},line width=0.8pt,dashed]  plot[domain=2.3398310085661786:2.8808423545124757,variable=\\t]({1.*3.078976141375616*cos(\\t r)+0.*3.078976141375616*sin(\\t r)},{0.*3.078976141375616*cos(\\t r)+1.*3.078976141375616*sin(\\t r)});\n'
                        '\\draw [shift={(0.0015065977442966637,0.23556291445715552)},line width=0.8pt,dashed]  plot[domain=0.7433374534911091:2.3042803758851607,variable=\\t]({1.*0.6099580128209037*cos(\\t r)+0.*0.6099580128209037*sin(\\t r)},{0.*0.6099580128209037*cos(\\t r)+1.*0.6099580128209037*sin(\\t r)});\n'
                        '\\draw [shift={(-1.2522529783658614,-0.8147320490019483)},line width=0.8pt,dashed]  plot[domain=0.37478916906229404:0.70981804643234,variable=\\t]({1.*2.2450403229328937*cos(\\t r)+0.*2.2450403229328937*sin(\\t r)},{0.*2.2450403229328937*cos(\\t r)+1.*2.2450403229328937*sin(\\t r)});\n'
                        '\\draw [shift={(0.8126679481418305,-0.4627640910175891)},line width=0.8pt,dashed]  plot[domain=2.3848979427362647:2.8450001420141278,variable=\\t]({1.*1.6771965723745104*cos(\\t r)+0.*1.6771965723745104*sin(\\t r)},{0.*1.6771965723745104*cos(\\t r)+1.*1.6771965723745104*sin(\\t r)});\n'
                        '\\draw [shift={(-4.074652796257185,-0.7097307251546232)},line width=0.8pt]  plot[domain=0.7445947433065315:2.3331877593376293,variable=\\t]({1.*0.9241196641511031*cos(\\t r)+0.*0.9241196641511031*sin(\\t r)},{0.*0.9241196641511031*cos(\\t r)+1.*0.9241196641511031*sin(\\t r)});\n'
                        '\\draw [shift={(-7.082244406990693,-3.386964441940012)},line width=0.8pt]  plot[domain=0.39063360069159375:0.7305698993864708,variable=\\t]({1.*4.950568200629588*cos(\\t r)+0.*4.950568200629588*sin(\\t r)},{0.*4.950568200629588*cos(\\t r)+1.*4.950568200629588*sin(\\t r)});\n'
                        '\\draw [shift={(-1.969414574987402,-2.607982693000769)},line width=0.8pt]  plot[domain=2.38950039701176:2.8459522154407684,variable=\\t]({1.*3.7568536784958084*cos(\\t r)+0.*3.7568536784958084*sin(\\t r)},{0.*3.7568536784958084*cos(\\t r)+1.*3.7568536784958084*sin(\\t r)});\n'
                        '\\draw [shift={(-4.113369602511252,-1.301401795357917)},line width=0.8pt]  plot[domain=0.7776739670023851:2.299076550356551,variable=\\t]({1.*0.5856078057002974*cos(\\t r)+0.*0.5856078057002974*sin(\\t r)},{0.*0.5856078057002974*cos(\\t r)+1.*0.5856078057002974*sin(\\t r)});\n'
                        '\\draw [shift={(-5.739270339345064,-3.0961770444592362)},line width=0.8pt]  plot[domain=0.5544020096943403:0.8236201267962598,variable=\\t]({1.*3.006569431137379*cos(\\t r)+0.*3.006569431137379*sin(\\t r)},{0.*3.006569431137379*cos(\\t r)+1.*3.006569431137379*sin(\\t r)});\n'
                        '\\draw [shift={(-2.464008025923585,-2.6945363044504838)},line width=0.8pt]  plot[domain=2.410143609678028:2.6912635573829746,variable=\\t]({1.*2.7400088596928915*cos(\\t r)+0.*2.7400088596928915*sin(\\t r)},{0.*2.7400088596928915*cos(\\t r)+1.*2.7400088596928915*sin(\\t r)});\n'
                        '\\draw [line width=0.8pt,dashed] (-1.550216232788688,0.015919995147472624)-- (-0.7912987377928602,0.027418745071651825);\n'
                        '\\draw [line width=0.8pt] (-5.563279956327232,-1.5134137447683609)-- (-4.930848710497376,-1.5019149948441817);\n'
                        '\\draw [line width=0.8pt] (-3.1830387220221357,-1.5134137447683609)-- (-2.5046124764955624,-1.5019149948441817);\n'
                        '\\draw [line width=0.8pt] (-4.14893371565319,0.211398743858519)-- (-0.04387999272121152,1.7292337338501733);\n'
                        '\\draw [line width=0.8pt,dashed] (-4.14893371565319,0.211398743858519)-- (-4.13743496572901,-1.5019149948441817);\n'
                        '\\draw [line width=0.8pt,dashed] (-3.1830387220221357,-1.5134137447683609)-- (0.8369474727567111,0.00712409815755994);\n'
                        '\\draw [line width=0.8pt] (-2.5046124764955624,-1.5019149948441817)-- (1.5701316607131717,0.00712409815755994);\n'
                        '\\draw [line width=0.8pt,dashed] (-5.563279956327232,-1.5134137447683609)-- (-1.550216232788688,0.015919995147472624);\n'
                        '\\draw [line width=0.8pt,dashed] (-4.930848710497376,-1.5019149948441817)-- (-0.7912987377928602,0.027418745071651825);\n'
                        '\\draw [line width=0.8pt,dashed] (-4.183429965425727,-0.72)-- (-0.04387999272121152,0.843829989688375);\n'
                        '\\draw [line width=1.pt ,dashed] (-0.7912987377928602,0.027418745071651825) -- (1.5,0.);\n'
                        '\\draw [line width=1.pt ,dashed] (1.9296147115754891E-4,0.019643973838957246) -- (0.013613756899684528,1.75);\n'
                        '\\draw (-0.720062460742486,1.4501179994251638) node[anchor=north west] {$0,5\\text{m}$};\n'
                        '\\draw (-0.48999020030042206,0.6755413892702163) node[anchor=north west] {$%s\\text{m}$};\n'
                        '\\draw (-0.32127054264290844,-0.5975251185092022) node[anchor=north west] {$%s\\text{m}$};\n'
                        '\\draw (-3.1895047228206397,-1.4948069342332502) node[anchor=north west] {$0,5\\text{m}$};\n'
                        '\\draw (-5.651277909550724,-1.4948069342332502) node[anchor=north west] {$0,5\\text{m}$};\n'
                        '\\draw (-4.493247531992336,-1.4487924821448375) node[anchor=north west] {$%s\\text{m}$};\n'
                        '\\draw [line width=0.8pt,dashed] (-4.930848710497376,-1.5019149948441817)-- (-3.1830387220221357,-1.5134137447683609);\n'
                        '\\draw [->,line width=1.pt ,dashed] (-0.7912987377928602,0.027418745071651825) -- (2.,0.);\n'
                        '\\draw [->,line width=1.pt ,dashed] (1.9296147115754891E-4,0.019643973838957246) -- (0.013613756899684528,2.1431887311206244);\n'
                        '\\draw (1.6726890478549794,0.07735351212085098) node[anchor=north west] {$x$};\n'
                        '\\draw (-0.32893961799097726,2.2246946095801112) node[anchor=north west] {$y$};\n'
                        '\\node at (0,0) [below]{$O$};\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                            'Gọi $(P_1):y=ax^2+b$ là parabol đi qua hai điểm $A\\left(%s;0\\right),A\\left(0;%s\\right)$\\\\ \n'
                        'Ta có hệ\\\\ \n'
                        '$\\heva{&0=a\\left(%s\\right)^2+%s\\\\&%s=b}\\Leftrightarrow \\heva{&a=%s\\\\&b=%s}\\Rightarrow (P_1):y=%sx^2+%s$.\\\\ \n'
                        'Gọi $(P_2):y=mx^2+n$ là parabol đi qua hai điểm $C\\left(%s;0\\right),D\\left(0;%s\\right)$\\\\ \n'
                        'Ta có hệ\\\\ \n'
                        '$\\heva{&0=m\\left(%s\\right)^2+%s\\\\&%s=n}\\Leftrightarrow \\heva{&m=%s\\\\&n=%s}\\Rightarrow (P_2):y=%sx^2+%s$.\\\\ \n'
                        'Ta có thể tích khối bê tông là\\\\ \n'
                        '$V=%s\\cdot\\left[\\displaystyle\\int\\limits_{%s}^{%s}\\left(%sx^2+%s\\right)\\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s}\\left(%sx^2+%s\\right)\\text{d}x\\right] %s$ m$^3$.'
                        %(latex(h2),latex(s),latex(d1),
                            latex(nsimplify(d1/2)),latex(nsimplify(h2)),latex(nsimplify(d1/2)),latex(nsimplify(h2)),latex(nsimplify(h2)),latex(nsimplify((-4*h2)/(d1*d1))),latex(nsimplify(h2)),latex(nsimplify((-4*h2)/(d1*d1))),latex(nsimplify(h2)),
                            latex(nsimplify(d2/2)),latex(nsimplify(h3)),latex(nsimplify(d2/2)),latex(nsimplify(h3)),latex(nsimplify(h3)),latex(nsimplify((-4*h3)/(d2*d2))),latex(nsimplify(h3)),latex(nsimplify((-4*h3)/(d2*d2))),latex(nsimplify(h3)),
                            latex(s),latex(nsimplify(c3)),latex(nsimplify(c4)),latex(nsimplify((-4*h3)/(d2*d2))),latex(nsimplify(h3)),latex(nsimplify(c1)),latex(nsimplify(c2)),latex(nsimplify((-4*h2)/(d1*d1))),latex(nsimplify(h2)),kqq

                        ))



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

