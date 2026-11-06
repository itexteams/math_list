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


def bt_dang9_p3_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(-9,-1)
                yd=-2*k
                c=yd
                xc=4*k
                xe=-xc
                xa=xc+k
                a=-Rational(c,xc**2)

                yg=3*k
                c1=yg
                a1=-Rational(c1,xc**2)

                f=a*x**2+c-a1*x**2-c1
                ngh=Rational(1,3)*a*x**3+c*x-Rational(1,3)*a1*x**3-c1*x

                ngha=Rational(1,3)*a*xa**3+c*xa-Rational(1,3)*a1*xa**3-c1*xa
                nghc=Rational(1,3)*a*xc**3+c*xc-Rational(1,3)*a1*xc**3-c1*xc
                nghe=Rational(1,3)*a*xe**3+c*xe-Rational(1,3)*a1*xe**3-c1*xe

                s1=abs(nghc-ngha)
                s2=abs(nghe-nghc)
                kq1=s1+s2

                h1=kq1   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Trên cửa sổ có dạng hình chữ nhật, họa sĩ thiết kế logo hình con cá cho một cửa hàng kinh doanh hải sản. Logo là hình phẳng được giới hạn bởi hai parabol với các kính thước được cho trong hình vẽ (đơn vị: dm). Diện tích của logo bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị). \n'
                                '}{'

                '\\definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1}  \n'
                '\\definecolor{ffffww}{rgb}{1,1,0.4}  \n'
                '\\scalebox{0.5}{ \n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                    '\\clip(-5.5,-5) rectangle (7,3);  \n'
                    '\\draw[line width=0pt,color=ffffww,fill=ffffww,fill opacity=0.72] {[smooth,samples=50,domain=-5.013930669924253:4] plot(\\x,{0-(1/8)*(\\x)^(2)+2})} -- (4,0) {[smooth,samples=50,domain=4:-5.013930669924253] -- plot(\\x,{3/16*(\\x)^(2)-3})} -- (-5.013930669924253,-1.1424375953508838) -- cycle; \n'
                    '\\draw [shift={(3.666691110716023,-0.14030868146050374)},line width=0.8pt]  plot[domain=2.192488531589774:4.19273042711605,variable=\\t]({1*1.364686318254823*cos(\\t r)+0*1.364686318254823*sin(\\t r)},{0*1.364686318254823*cos(\\t r)+1*1.364686318254823*sin(\\t r)}); \n'
                    '\\draw [samples=50,rotate around={-180.:(0.,2.)},xshift=0.cm,yshift=2.cm,line width=1.pt,domain=-4:5)] plot (\\x,{(\\x)^2/2/4.0}); \n'
                    '\\draw [samples=50,rotate around={-180.:(0.,2.)},xshift=0.cm,yshift=2.cm,line width=1.pt,domain=-4:5)] plot (\\x,{-3*(\\x)^2/4/4+5.0}); \n'
                    '\\draw (-0.,0.05096119250744481) node[anchor=north west] {O}; \n'
                    '\\draw (-4.128952697169539,0.861012039243977) node[anchor=north west] {$C$}; \n'
                    '\\draw (-5.499807976262131,2.0657030420829225) node[anchor=north west] {$B$}; \n'
                    '\\draw (4.200031650044543,-0.0736620146827909) node[anchor=north west] {$E$}; \n'
                    '\\draw (-0.49410915412099937,-2.275338675043622) node[anchor=north west] {$G$}; \n'
                    '\\draw (-0.47333861958929346,2.647278008970689) node[anchor=north west] {$D$}; \n'
                    '\\draw (-5.520578510793837,-0.8006307232924993) node[anchor=north west] {$A$}; \n'
                    '\\draw (2.185289800469067,1.88) node[anchor=north west] {$y=f(x)$}; \n'
                    '\\draw (-4.793609802184129,-3.6) node[anchor=north west] {$%s$ dm}; \n'
                    '\\draw (-2.1972929857208863,-3.6) node[anchor=north west] {$%s$ dm}; \n'
                    '\\draw (1.6452559026447124,-3.6) node[anchor=north west] {$%s$ dm}; \n'
                    '\\draw (5.7578217399224885,-0.8421717923559112) node[anchor=north west] {$%s$ dm}; \n'
                    '\\draw (5.716280670859077,1.5) node[anchor=north west] {$%s$ dm}; \n'
                    '\\draw [->,line width=0.4pt] (-6.58799407477297,0) -- (5.504139016184864,0); \n'
                    '\\draw [->,line width=0.4pt] (0,-4) -- (0,3.3870166045168313); \n'
                    '\\draw (-0.49410915412099937,3.4) node[anchor=north west] {$y$}; \n'
                    '\\draw (4.927000358654251,0.5) node[anchor=north west] {$x$}; \n'
                    '\\draw [line width=0.4pt] (-5.025647675410276,2.017288254390636)-- (4,2); \n'
                    '\\draw [line width=0.4pt] (4,2)-- (3.9631946222928924,-3.0549870421704326); \n'
                    '\\draw [line width=0.4pt] (3.9631946222928924,-3.0549870421704326)-- (-5.025647675410276,-3.012183031228989); \n'
                    '\\draw [line width=0.4pt] (-5.025647675410276,-3.012183031228989)-- (-5.025647675410276,2.017288254390636); \n'
                    '\\draw [->,line width=0.4pt] (-3.9953828730873333,-3.6318276911737413) -- (-5.009695366012641,-3.6318276911737413); \n'
                    '\\draw [->,line width=0.4pt] (-5.009695366012641,-3.6318276911737413) -- (-3.9953828730873333,-3.6318276911737413); \n'
                    '\\draw [->,line width=0.4pt] (-3.9953828730873333,-3.6318276911737413) -- (0,-3.632841189879921); \n'
                    '\\draw [->,line width=0.4pt] (0,-3.632841189879921) -- (-3.9953828730873333,-3.6318276911737413); \n'
                    '\\draw [->,line width=0.4pt] (0,-3.632841189879921) -- (4.005998633234336,-3.632841189879921); \n'
                    '\\draw [->,line width=0.4pt] (4.005998633234336,-3.632841189879921) -- (0,-3.632841189879921); \n'
                    '\\draw [->,line width=0.4pt] (5.708796114333198,0.008811194335592005) -- (5.703111922280682,-3.0551979862915477); \n'
                    '\\draw [->,line width=0.4pt] (5.703111922280682,-3.0551979862915477) -- (5.708796114333198,0.008811194335592187); \n'
                    '\\draw [->,line width=0.4pt] (5.708796114333198,0.008811194335592005) -- (5.696164576438735,1.9919626437661464); \n'
                    '\\draw [->,line width=0.4pt] (5.696164576438735,1.9919626437661464) -- (5.708796114333198,0.008811194335591965); \n'
                    '\\draw (2.039896058747125,-2) node[anchor=north west] {$y=g(x)$}; \n'
                    '\\begin{scriptsize}  \n'
                        '\\draw [fill=ududff] (2.98901,0.3148439999999999) circle (3.5pt); \n'
                    '\\end{scriptsize}  \n'
                '\\end{tikzpicture} }  \n'

                                '}'
                                %(latex(-k),latex(xe),latex(xe),latex(-3*k),latex(-2*k)
                                ))

                # Nội dung lời giải
                loigiai = ('Giả sử parabol $y=f(x)$ cho bởi $f(x)=ax^2+bx+c, (a\\ne 0)$. \\\\ \n'
                        'Do parabol $y=f(x)$ đi qua điểm $D(0;%s)$ nên $c=%s$, suy ra $f(x)=ax^2+bx+%s, (a\\ne 0)$. \\\\ \n'
                        'Vì parabol $y=f(x)$ đi qua các điểm $C(%s; 0), E(%s; 0)$ nên ta có \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& %s a+%s b+%s=0\\\\& %s a+%s b+%s=0} \\Leftrightarrow \\heva{& a=%s\\\\& b=0.}$ \\\\ \n'
                        'Vậy $f(x)=%s x^2+%s$. \\\\ \n'

                        'Giả sử parabol $y=g(x)$ cho bởi $f(x)=a_1 x^2+b_1 x+c_1, (a_1 \\ne 0)$. \\\\ \n'
                            'Do parabol $y=g(x)$ đi qua điểm $G(0;%s)$ nên $c_1=%s$, suy ra $f(x)=a_1 x^2+b_1 x+%s, (a_1 \\ne 0)$. \\\\ \n'
                            'Vì parabol $y=g(x)$ đi qua các điểm $C(%s; 0), E(%s; 0)$ nên ta có \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& %s a_1+%s b_1+%s=0\\\\& %s a_1+%s b_1+%s=0} \\Leftrightarrow \\heva{& a_1=%s\\\\& b_1=0.}$ \\\\ \n'
                            'Vậy $g(x)=%s x^2+%s$. \\\\ \n'

                            'Ta có $f(x)-g(x)=%s$.\\\\ \n'

                            'Diện tích của logo là \\\\ \n'
                            '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x)-g(x) \\right|\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x)-g(x) \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x)-g(x) \\right|\\text{d}x$.\\\\ \n'
                            '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| %s \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| %s \\right|\\text{d}x=%s+%s=%s$.\\\\ \n'
                            'Vậy diện tích logo xấp xỉ bằng $%s$ dm$^2$.'


                        %(latex(yd),latex(yd),latex(c),
                            latex(xc),latex(xe),
                            latex(xc**2),latex(xc),latex(c),
                            latex(xe**2),latex(xe),latex(c),latex(a),
                            latex(a),latex(c),

                            latex(yg),latex(yg),latex(c),
                            latex(xc),latex(xe),
                            latex(xc**2),latex(xc),latex(c1),
                            latex(xe**2),latex(xe),latex(c1),latex(a1),
                            latex(a1),latex(c1),

                            latex(f),

                            latex(xa),latex(xe),latex(xa),latex(xc),latex(xc),latex(xe),
                            latex(xa),latex(xc),latex(f),latex(xc),latex(xe),latex(f),latex(s1),latex(s2),latex(kq1),
                            latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content 
