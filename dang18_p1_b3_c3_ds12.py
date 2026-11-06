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


def bt_dang18_p1_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x=symbols('x')
                k=randint(1,5)
                a=-Rational(1,100*k**2)
                b=4*k**2
                f=a*x**2+b
                c=b+1
                d=randint(6,10)
                s1=integrate(c-f, (x, -sqrt(-b/a), sqrt(-b/a)))

                du = ['$%s$ m$^3$'%(latex(s1*d)),
                    ]
                da= random.choice(du)
                s = ['$%s$ m$^3$'%(latex(s1*d+1)),
                    '$%s$ m$^3$'%(latex(s1*d+2)),
                    '$%s$ m$^3$'%(latex(s1*d+3)),
                    '$%s$ m$^3$'%(latex(s1*d-1)),
                    '$%s$ m$^3$'%(latex(s1*d-2)),
                    '$%s$ m$^3$'%(latex(s1*d-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Hình bên dưới là mặt cắt dọc của một chiếc cầu bê tông (phần tô đậm, các đơn vị đều đo bằng mét).
                                \\begin{center}
                \\definecolor{ffxfqq}{rgb}{1.,0.4980392156862745,0.}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-6.325367965367974,-1.195324675324675) rectangle (6.159480519480513,3.3068398268398274);
                    \\draw[line width=0.8pt,color=ffxfqq,fill=ffxfqq,fill opacity=0.4399999976158142] {[smooth,samples=50,domain=-5.0:5.0] plot(\\x,{2.0})} -- (5.,0.) {[smooth,samples=50,domain=5.0:-5.0] -- plot(\\x,{0-0.04*(\\x)^(2)+1})} -- (-5.,2.) -- cycle;
                    \\draw [line width=1.pt] (-5.,0.)-- (-5.,2.);
                    \\draw [line width=1.pt] (-5.,2.)-- (5.,2.);
                    \\draw [line width=1.pt] (5.,2.)-- (5.,0.);
                    \\draw [shift={(0.,-12.)},line width=1.pt]  plot[domain=1.1760052070951352:1.965587446494658,variable=\\t]({1.*13.*cos(\\t r)+0.*13.*sin(\\t r)},{0.*13.*cos(\\t r)+1.*13.*sin(\\t r)});
                    \\draw [->,line width=1.pt] (-6.,0.) -- (6.,0.);
                    \\draw [->,line width=1.pt] (0.,-1.) -- (0.,3.);
                    \\draw (-0.6,0) node[anchor=north west] {$O$};
                    \\draw (5.5,0) node[anchor=north west] {$x$};
                    \\draw (-0.5,3) node[anchor=north west] {$y$};
                    \\draw (0,2.6) node[anchor=north west] {$%s$};
                    \\draw (0.2,2) node[anchor=north west] {$y=%s$};
                \\end{tikzpicture}
            \\end{center}
            Biết chiều rộng của cầu bằng $%s$ m. Khối lượng bê tông để làm cầu là'''
                                %(latex(c),latex(f),latex(d)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Từ hình vẽ ta thấy vòm gầm cầu là parabol $y=%s$. \\\\
                        Giao điểm của parabol và trục $Ox$ là nghiệm của phương trình \\\\
                            $%s=0 \\Leftrightarrow x^2=%s \\Leftrightarrow x=\\pm %s$.
                        Bề mặt của cầu là đường thẳng $y=%s$. \\\\
                        Khi đó diện tích mặt cắt là $S=\\int \\limits_{%s}^{%s} \\left[ %s-\\left(%s\\right) \\right] \\text{d}x=%s$. \\\\
                        Vậy khối lượng bên tông để làm cầu là $V=%s \\cdot %s=%s$ m$^3$.'''
                        %(latex(f),latex(f),
                        latex(-Rational(b,a)),latex(sqrt(-b/a)),
                        latex(c),
                        latex(-sqrt(-b/a)),latex(sqrt(-b/a)),
                        latex(c),latex(f),latex(s1),
                        latex(s1),latex(d),latex(s1*d)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

