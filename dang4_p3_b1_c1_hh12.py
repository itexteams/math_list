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


def bt_dang4_p3_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(800,1000)
                b=randint(810,900)
                while a>=b+5:
                    a=randint(800,1000)
                    b=randint(810,1000)

                x0=Rational(a**2,b**2)


                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = (

                    '''\\begin{center}
                        \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                            \\clip(-2$zz$0594244062865115,-0$zz$8597596510951809) rectangle (8$zz$80637167553614,3$zz$277517414127853);
                            \\draw [line width=1$zz$pt] (0$zz$9811784690758546,1$zz$4367721899780055)-- (6$zz$184819389335351,1$zz$8124361066812318);
                            \\draw [line width=1$zz$pt] (2$zz$7342767470242406,1$zz$144589143653274)-- (3$zz$8195280619446708,1$zz$1863295788425214);
                            \\draw [line width=1$zz$pt] (2$zz$7342767470242406,1$zz$144589143653274)-- (0$zz$17419672208374032,-0$zz$20501826079905697);
                            \\draw [line width=1$zz$pt] (0$zz$17419672208374032,-0$zz$20501826079905697)-- (0$zz$8142167283188654,-0$zz$20501826079905697);
                            \\draw [line width=1$zz$pt] (0$zz$8142167283188654,-0$zz$20501826079905697)-- (3$zz$8195280619446708,1$zz$1863295788425214);
                            \\draw [line width=1$zz$pt] (3$zz$4737670656435244,1$zz$6167184255590943)-- (4$zz$3760671978013015,2$zz$285494372159368);
                            \\draw [line width=1$zz$pt] (4$zz$3760671978013015,2$zz$285494372159368)-- (4$zz$654336765729616,2$zz$299407850555784);
                            \\draw [line width=1$zz$pt] (4$zz$654336765729616,2$zz$299407850555784)-- (4$zz$34876925104017,1$zz$6798870325262318);
                            \\draw [line width=1$zz$pt] (0$zz$41072585482280827,1$zz$1724161004461056)-- (1$zz$,1$zz$);
                            \\draw [line width=1$zz$pt] (1$zz$,1$zz$)-- (2$zz$222970806991631,0$zz$8750419904839087);
                            \\draw [line width=1$zz$pt] (3$zz$181928474430865,0$zz$8911445846231665)-- (6$zz$,1$zz$);
                            \\draw [line width=1$zz$pt] (6$zz$,1$zz$)-- (6$zz$783098960381228,1$zz$0471947948783635);
                            \\draw [line width=1$zz$pt] (0$zz$9811784690758546,1$zz$4367721899780055)-- (0$zz$27159107085865064,2$zz$1463595881952107);
                            \\draw [line width=1$zz$pt] (0$zz$27159107085865064,2$zz$1463595881952107)-- (-0$zz$13189980263740647,2$zz$132446109798795);
                            \\draw [line width=1$zz$pt] (-0$zz$13189980263740647,2$zz$132446109798795)-- (0$zz$2855045492550664,1$zz$408945233185174);
                            \\draw [line width=1$zz$pt] (0$zz$2855045492550664,1$zz$408945233185174)-- (-0$zz$5493041545298794,1$zz$3672047979959265);
                            \\draw [line width=1$zz$pt] (-0$zz$5493041545298794,1$zz$3672047979959265)-- (-0$zz$0901593674481592,1$zz$2558969708246004);
                            \\draw [line width=1$zz$pt] (-0$zz$0901593674481592,1$zz$2558969708246004)-- (0$zz$7585628147332023,1$zz$214156535635353);
                            \\draw [line width=1$zz$pt] (0$zz$7585628147332023,1$zz$214156535635353)-- (0$zz$2855045492550664,1$zz$408945233185174);
                            \\draw [shift={(6$zz$074813735018881,1$zz$2251799874083962)},line width=1$zz$pt]  plot[domain=0$zz$49459137750009474:1$zz$3856208905686307,variable=\\t]({1$zz$*0$zz$5974704960121341*cos(\\t r)+0$zz$*0$zz$5974704960121341*sin(\\t r)},{0$zz$*0$zz$5974704960121341*cos(\\t r)+1$zz$*0$zz$5974704960121341*sin(\\t r)});
                            \\draw [shift={(6$zz$587852905594786,1$zz$058584232286239)},line width=1$zz$pt]  plot[domain=0$zz$592304597492696:1$zz$542300821416676,variable=\\t]({1$zz$*0$zz$45038113325492457*cos(\\t r)+0$zz$*0$zz$45038113325492457*sin(\\t r)},{0$zz$*0$zz$45038113325492457*cos(\\t r)+1$zz$*0$zz$45038113325492457*sin(\\t r)});
                            \\draw [shift={(6$zz$843239899188446,1$zz$2069062524702845)},line width=1$zz$pt]  plot[domain=-0$zz$6555079135676412:0$zz$7170269657085766,variable=\\t]({1$zz$*0$zz$15691215864180832*cos(\\t r)+0$zz$*0$zz$15691215864180832*sin(\\t r)},{0$zz$*0$zz$15691215864180832*cos(\\t r)+1$zz$*0$zz$15691215864180832*sin(\\t r)});
                            \\draw [shift={(6$zz$785183080257137,1$zz$3389882033765672)},line width=1$zz$pt]  plot[domain=4$zz$705246651681846:5$zz$387834813550572,variable=\\t]({1$zz$*0$zz$2918008512644484*cos(\\t r)+0$zz$*0$zz$2918008512644484*sin(\\t r)},{0$zz$*0$zz$2918008512644484*cos(\\t r)+1$zz$*0$zz$2918008512644484*sin(\\t r)});
                            \\draw [line width=1$zz$pt] (0$zz$9811784690758545,1$zz$4367721899780055)-- (0$zz$5866131003610235,1$zz$4460926356119066);
                            \\draw [shift={(6$zz$04134456220191,2$zz$631541588057621)},line width=1$zz$pt]  plot[domain=4$zz$723663093549282:5$zz$105661397036152,variable=\\t]({1$zz$*0$zz$9973664608131186*cos(\\t r)+0$zz$*0$zz$9973664608131186*sin(\\t r)},{0$zz$*0$zz$9973664608131186*cos(\\t r)+1$zz$*0$zz$9973664608131186*sin(\\t r)});
                            \\draw [shift={(6$zz$102191438512533,2$zz$31349033975011)},line width=1$zz$pt]  plot[domain=4$zz$650415385181313:5$zz$266480344393735,variable=\\t]({1$zz$*0$zz$8680355436044007*cos(\\t r)+0$zz$*0$zz$8680355436044007*sin(\\t r)},{0$zz$*0$zz$8680355436044007*cos(\\t r)+1$zz$*0$zz$8680355436044007*sin(\\t r)});
                            \\draw [line width=1$zz$pt] (6$zz$052588746344307,1$zz$6342385120181164)-- (6$zz$048430583993901,1$zz$447121206249837);
                            \\draw [line width=1$zz$pt] (6$zz$223073402710963,1$zz$650871161419741)-- (6$zz$372767247325586,1$zz$4887028297538991);
                            \\draw [->,line width=1$zz$pt] (3$zz$700100771352949,1$zz$4266303060017589) -- (3$zz$6674380576801355,2$zz$798464280259923);
                            \\draw [->,line width=1$zz$pt] (3$zz$7109883425772203,1$zz$0020150282551843) -- (3$zz$7109883425772203,-0$zz$15206752151755665);
                            \\draw [->,line width=1$zz$pt] (6$zz$8357212839430535,1$zz$2197664527406071) -- (8$zz$327318541668207,1$zz$2742043088619628);
                            \\draw [->,line width=1$zz$pt] (0$zz$40116669039877795,1$zz$132665882946438) -- (-1$zz$014217568756477,1$zz$0891155980493534);
                            \\draw (3$zz$808976483595661,3) node[anchor=north west] {Lực nâng};
                            \\draw (3$zz$8198640548199325,0$zz$5) node[anchor=north west] {Trọng lực};
                            \\draw (7,2) node[anchor=north west] {Lực đẩy};
                            \\draw (-2,1$zz$2) node[anchor=north west] {Lực cản};
                            \\draw (-2,0$zz$7) node[anchor=north west] {của không khí};
                        \\end{tikzpicture}
                        \\end{center}
                    '''


                    'Khi chuyển động trong không gian, máy bay luôn chịu tác động của bốn lực chính:lực đẩy của động cơ, lực cản của không khí, trọng lực và lực nâng khí động học$zz$ (Hình vẽ)'
                                ' Lực cản của không khí ngược hướng với lực đẩy của động cơ và có độ lớn tỉ lệ thuận với bình phương vận tốc máy bay$zz$ Một chiếc máy bay tăng tốc từ $%s$ (km/h) lên $%s$ (km/h), trong quá trình tăng tốc máy bay giữ nguyên hướng bay$zz$'
                                ' Lực cản của không khí khi máy máy bay đạt vận tốc $%s$(km/h) và $%s$(km/h) lần lượt biểu diễn bởi hai vec tơ $\\vec{F_1}$ và $\\vec{F_2}$ với $\\vec{F_1}=k\\vec{F_2}$ $(k\\in \\mathbb{R};k>0)$$zz$'
                                ' Giá trị của $k$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm)$zz$\\\\ \n'

                                %(latex(a),latex(b),latex(a),latex(b))
                                )

                # Nội dung lời giải
                loigiai = ('Vì trong quá trình máy bay tăng tốc từ $%s$(km/h) lên $%s$(km/h), máy bay giữ nguyên hướng bay nên hai vectơ $\\vec{F_1}$ và $\\vec{F_2}$ có cùng hướng và $\\vec{F_1}=k\\vec{F_2}$ $(k>0)$$zz$\\\\ \n'
                        'Gọi $v_1, v_2$ lần lượt là vận tốc chiếc máy bay khi đạt $%s$(km/h) và $%s$(km/h)$zz$\\\\ \n'
                        'Suy ra $v_1=%s$(km/h), $v_2=%s$(km/h)$zz$\\\\ \n'
                        'Vì lực cản của không khí ngược hướng với lực đẩy của động cơ và có độ lớn tỷ lệ thuận với bình phương vận tốc máy bay nên\\\\ \n'
                        '\\hspace*{1cm} $\\left|\\dfrac{\\vec{F_1}}{\\vec{F_2}}\\right|=\\dfrac{v_1^2}{v_2^2}=\\dfrac{%s^2}{%s^2}=%s\\Rightarrow \\left|\\vec{F_1}\\right|=%s\\left|\\vec{F_2}\\right| \\Rightarrow \\vec{F_1}=%s\\vec{F_2}$$zz$\\\\ \n'
                        'Từ đó suy ra $k=%s \\approx %s$$zz$'

                            %(latex(a),latex(b),
                            latex(a),latex(b),
                            latex(a),latex(b),
                            latex(a),latex(b),latex(x0),latex(x0),latex(x0),
                            latex(x0),latex(kq))
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

