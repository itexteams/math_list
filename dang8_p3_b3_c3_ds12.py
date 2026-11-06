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


def bt_dang8_p3_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=0
                b=randint(4,9)
                c=randint(1,5) 
                d=randint(1,5) 
                f=sqrt(c+x**2/d)
                y=c*x+x**3/(3*d)
                kq1=c*b+Rational(b**3,3*d)
                h1=kq1    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một bình chứa nước có dạng như hình vẽ$zz$ Biết rằng khi nước trong bình có chiều cao $x$ (dm) với $0 \\le x \\le %s$ thì mặt nước là hình vuông có cạnh $%s$ dm$zz$ Dung tích của bình bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$\n'
                                '}{' 
                                '\\definecolor{ffqqqq}{rgb}{1$zz$,0$zz$,0$zz$}  \n'
                                '\\definecolor{qqffff}{rgb}{0$zz$,1$zz$,1$zz$}  \n'
                                '\\scalebox{0$zz$7}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                    '\\clip(-1$zz$6434039969278025,-0$zz$5512761035088748) rectangle (6,5);  \n'
                                    '\\fill[color=qqffff,fill=qqffff,fill opacity=0$zz$1] (-0$zz$26398778736946554,2$zz$0076323234619364) -- (0$zz$7587916351283395,2$zz$992252909262609) -- (3$zz$2486509176238596,2$zz$992252909262609) -- (2$zz$2477341917718348,1$zz$998882855167637) -- cycle;  \n'
                                    '\\fill[color=qqffff,fill=qqffff,fill opacity=0$zz$1] (-0$zz$26398778736946554,2$zz$0076323234619364) -- (-0$zz$21674227366772492,1$zz$804417271457252) -- (-0$zz$15989342881409563,1$zz$526867687261142) -- (-0$zz$0845753454048932,1$zz$0651963819056973) -- (-0$zz$057517724285101934,0$zz$8497930420464672) -- (-0$zz$031162789531729018,0$zz$5844429563131125) -- (-0$zz$008258151827696736,0$zz$2382441175635883) -- (0$zz$,0$zz$) -- (2$zz$,0$zz$) -- (3$zz$,1$zz$) -- (2$zz$9870646277420487,1$zz$2703263081230274) -- (2$zz$9891198055663466,1$zz$558750391577459) -- (3$zz$004106572101147,1$zz$8081410043558175) -- (3$zz$0299366055608203,2$zz$0461569137363687) -- (3$zz$066306107314637,2$zz$2792148604715265) -- (3$zz$109938728822624,2$zz$494896110150188) -- (3$zz$1628812655959226,2$zz$7085855492715987) -- (3$zz$2486509176238596,2$zz$992252909262609) -- (0$zz$7587916351283395,2$zz$992252909262609) -- cycle;  \n'
                                    '\\draw [shift={(-9$zz$314380483264664,-0$zz$20359512081616524)}] plot[domain=0$zz$021854669347379216:0$zz$468102656906349,variable=\\t]({1$zz$*9$zz$316605323842039*cos(\\t r)+0$zz$*9$zz$316605323842039*sin(\\t r)},{0$zz$*9$zz$316605323842039*cos(\\t r)+1$zz$*9$zz$316605323842039*sin(\\t r)});  \n'
                                    '\\draw [shift={(10$zz$806715534676307,-0$zz$07667888366907748)}] plot[domain=2$zz$6603419723721977:3$zz$13288600855366,variable=\\t]({1$zz$*8$zz$80704934469597*cos(\\t r)+0$zz$*8$zz$80704934469597*sin(\\t r)},{0$zz$*8$zz$80704934469597*cos(\\t r)+1$zz$*8$zz$80704934469597*sin(\\t r)});  \n'
                                    '\\draw [shift={(-7$zz$642666314298063,0$zz$9643334214254842)},dash pattern=on 2pt off 2pt]  plot[domain=0$zz$0041267792607418636:0$zz$48583054699298645,variable=\\t]({1$zz$*8$zz$642739908450888*cos(\\t r)+0$zz$*8$zz$642739908450888*sin(\\t r)},{0$zz$*8$zz$642739908450888*cos(\\t r)+1$zz$*8$zz$642739908450888*sin(\\t r)});  \n'
                                    '\\draw [shift={(8$zz$07454773569566,1$zz$3782945991141278)}] plot[domain=2$zz$349641498061153:3$zz$216002468577289,variable=\\t]({1$zz$*5$zz$088628648818155*cos(\\t r)+0$zz$*5$zz$088628648818155*sin(\\t r)},{0$zz$*5$zz$088628648818155*cos(\\t r)+1$zz$*5$zz$088628648818155*sin(\\t r)});  \n'
                                    '\\draw (0$zz$,5$zz$)-- (4$zz$5,5$zz$);  \n'
                                    '\\draw (0$zz$,5$zz$)-- (-1$zz$,4$zz$);  \n'
                                    '\\draw (-1$zz$,4$zz$)-- (3$zz$,4$zz$);  \n'
                                    '\\draw (3$zz$,4$zz$)-- (4$zz$5,5$zz$);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (1$zz$,1$zz$)-- (0$zz$,0$zz$);  \n'
                                    '\\draw (0$zz$,0$zz$)-- (2$zz$,0$zz$);  \n'
                                    '\\draw (2$zz$,0$zz$)-- (3$zz$,1$zz$);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,1$zz$)-- (1$zz$,1$zz$);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$7587916351283395,2$zz$992252909262609)-- (3$zz$2486509176238596,2$zz$992252909262609);  \n'
                                    '\\draw (3$zz$2486509176238596,2$zz$992252909262609)-- (2$zz$2477341917718348,1$zz$998882855167637);  \n'
                                    '\\draw (2$zz$2477341917718348,1$zz$998882855167637)-- (-0$zz$26398778736946554,2$zz$0076323234619364);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (-0$zz$26398778736946554,2$zz$0076323234619364)-- (0$zz$7587916351283395,2$zz$992252909262609);  \n'
                                    '\\draw [shift={(-7$zz$642666314298153,0$zz$9643334214254461)}] plot[domain=0$zz$35889399760678975:0$zz$4858305469929855,variable=\\t]({1$zz$*8$zz$642739908450986*cos(\\t r)+0$zz$*8$zz$642739908450986*sin(\\t r)},{0$zz$*8$zz$642739908450986*cos(\\t r)+1$zz$*8$zz$642739908450986*sin(\\t r)});  \n'
                                    '\\draw [color=qqffff] (-0$zz$26398778736946554,2$zz$0076323234619364)-- (0$zz$7587916351283395,2$zz$992252909262609);  \n'
                                    '\\draw [color=qqffff] (0$zz$7587916351283395,2$zz$992252909262609)-- (3$zz$2486509176238596,2$zz$992252909262609);  \n'
                                    '\\draw [color=qqffff] (3$zz$2486509176238596,2$zz$992252909262609)-- (2$zz$2477341917718348,1$zz$998882855167637);  \n'
                                    '\\draw [color=qqffff] (2$zz$2477341917718348,1$zz$998882855167637)-- (-0$zz$26398778736946554,2$zz$0076323234619364);  \n'
                                    '\\draw [color=qqffff] (-0$zz$26398778736946554,2$zz$0076323234619364)-- (-0$zz$21674227366772492,1$zz$804417271457252);  \n'
                                    '\\draw [color=qqffff] (-0$zz$21674227366772492,1$zz$804417271457252)-- (-0$zz$15989342881409563,1$zz$526867687261142);  \n'
                                    '\\draw [color=qqffff] (-0$zz$15989342881409563,1$zz$526867687261142)-- (-0$zz$0845753454048932,1$zz$0651963819056973);  \n'
                                    '\\draw [color=qqffff] (-0$zz$0845753454048932,1$zz$0651963819056973)-- (-0$zz$057517724285101934,0$zz$8497930420464672);  \n'
                                    '\\draw [color=qqffff] (-0$zz$057517724285101934,0$zz$8497930420464672)-- (-0$zz$031162789531729018,0$zz$5844429563131125);  \n'
                                    '\\draw [color=qqffff] (-0$zz$031162789531729018,0$zz$5844429563131125)-- (-0$zz$008258151827696736,0$zz$2382441175635883);  \n'
                                    '\\draw [color=qqffff] (-0$zz$008258151827696736,0$zz$2382441175635883)-- (0$zz$,0$zz$);  \n'
                                    '\\draw [color=qqffff] (0$zz$,0$zz$)-- (2$zz$,0$zz$);  \n'
                                    '\\draw [color=qqffff] (2$zz$,0$zz$)-- (3$zz$,1$zz$);  \n'
                                    '\\draw [color=qqffff] (3$zz$,1$zz$)-- (2$zz$9870646277420487,1$zz$2703263081230274);  \n'
                                    '\\draw [color=qqffff] (2$zz$9870646277420487,1$zz$2703263081230274)-- (2$zz$9891198055663466,1$zz$558750391577459);  \n'
                                    '\\draw [color=qqffff] (2$zz$9891198055663466,1$zz$558750391577459)-- (3$zz$004106572101147,1$zz$8081410043558175);  \n'
                                    '\\draw [color=qqffff] (3$zz$004106572101147,1$zz$8081410043558175)-- (3$zz$0299366055608203,2$zz$0461569137363687);  \n'
                                    '\\draw [color=qqffff] (3$zz$0299366055608203,2$zz$0461569137363687)-- (3$zz$066306107314637,2$zz$2792148604715265);  \n'
                                    '\\draw [color=qqffff] (3$zz$066306107314637,2$zz$2792148604715265)-- (3$zz$109938728822624,2$zz$494896110150188);  \n'
                                    '\\draw [color=qqffff] (3$zz$109938728822624,2$zz$494896110150188)-- (3$zz$1628812655959226,2$zz$7085855492715987);  \n'
                                    '\\draw [color=qqffff] (3$zz$1628812655959226,2$zz$7085855492715987)-- (3$zz$2486509176238596,2$zz$992252909262609);  \n'
                                    '\\draw [color=qqffff] (3$zz$2486509176238596,2$zz$992252909262609)-- (0$zz$7587916351283395,2$zz$992252909262609);  \n'
                                    '\\draw [color=qqffff] (0$zz$7587916351283395,2$zz$992252909262609)-- (-0$zz$26398778736946554,2$zz$0076323234619364);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt,color=ffqqqq] (1$zz$3908601006173285,0$zz$48330298926073434)-- (1$zz$4340912912779593,4$zz$449764732373605);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt,color=ffqqqq] (1$zz$4340912912779593,4$zz$449764732373605)-- (5$zz$281667260074105,4$zz$438956934708448);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt,color=ffqqqq] (1$zz$3908601006173285,0$zz$48330298926073434)-- (5$zz$270859462408947,0$zz$4724951915955766);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt,color=ffqqqq] (1$zz$4131222141435968,2$zz$525851905295852)-- (4$zz$071193921576441,2$zz$5151689503103793);  \n'
                                    '\\draw [->] (3$zz$790191182282341,1$zz$4776203744552414) -- (3$zz$7793880981156036,2$zz$516341736006045);  \n'
                                    '\\draw [->] (3$zz$790191182282341,1$zz$4776203744552414) -- (3$zz$801070594751785,0$zz$4765893110040924);  \n'
                                    '\\draw [->] (4$zz$914202139458743,2$zz$1585116273601757) -- (4$zz$935817734789058,4$zz$384917946382659);  \n'
                                    '\\draw [->] (4$zz$914202139458743,2$zz$1585116273601757) -- (4$zz$9250099371239004,0$zz$5265341799213652);  \n'
                                    '\\draw (3$zz$8687084082831755,1$zz$9576854050699066) node[anchor=north west] {$x$};  \n'
                                    '\\draw (5$zz$009145457637171,2$zz$9333926584060994) node[anchor=north west] {$%s$};  \n'
                                    '\\draw (0$zz$,0$zz$)-- (2$zz$,0$zz$);  \n'
                                    '\\draw (2$zz$,0$zz$)-- (3$zz$,1$zz$);  \n'
                                    '\\draw [shift={(-9$zz$31438048326477,-0$zz$20359512081617942)}] plot[domain=0$zz$021854669347380486:0$zz$23962937933850784,variable=\\t]({1$zz$*9$zz$316605323842145*cos(\\t r)+0$zz$*9$zz$316605323842145*sin(\\t r)},{0$zz$*9$zz$316605323842145*cos(\\t r)+1$zz$*9$zz$316605323842145*sin(\\t r)});  \n'
                                    '\\draw [shift={(8$zz$074547735695594,1$zz$378294599114136)}] plot[domain=2$zz$818849155129027:3$zz$216002468577291,variable=\\t]({1$zz$*5$zz$08862864881809*cos(\\t r)+0$zz$*5$zz$08862864881809*sin(\\t r)},{0$zz$*5$zz$08862864881809*cos(\\t r)+1$zz$*5$zz$08862864881809*sin(\\t r)});  \n'
                                '\\end{tikzpicture} } \n'
                                '}'
                                %(latex(b),latex(f),
                                latex(b)
                                ))

                # Nội dung lời giải
                loigiai = ('Diện tích của mặt nước là \\\\ \n'
                        '\\hspace*{1cm} $S(x)=\\left( %s \\right)^2=%s$ (dm$^2$)$zz$ \\\\ \n'
                        'Dung tích của bình là \\\\ \n'
                        '\\hspace*{1cm} $V=\\displaystyle\\int\\limits_{%s}^{%s} S(x) \\text{d}x =\\displaystyle\\int\\limits_{%s}^{%s} \\left( %s \\right) \\text{d}x=%s \\approx %s$ (dm$^3$)$zz$'

                        %(latex(f),latex(f**2),
                            latex(a),latex(b),latex(a),latex(b),latex(f**2),latex(kq1),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content 

