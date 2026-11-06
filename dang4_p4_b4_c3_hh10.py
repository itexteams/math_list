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


def bt_dang4_p4_b4_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                h1=randint(3,12)
                h=h1*10
                a=randint(5,30)
                b=randint(8,40)



                while a>=b:
                    x=symbols('x')
                    y=symbols('y')
                    h1=randint(3,12)
                    h=h1*10
                    a=randint(5,30)
                    b=randint(8,40)
                oh=Rational(2*h,5)
                ok=Rational(3*h,5)
                x1=sqrt(Rational(b**2*a**2+oh**2*a**2,b**2))
                x2=sqrt(Rational(b**2*a**2+ok**2*a**2,b**2))
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                    '''Một cái tháp làm nguội của một nhà máy có mặt cắt là hình hypebol $(H)$ có phương trình $\\dfrac{x^2}{%s^2}-\\dfrac{y^2}{%s^2}= 1$. Biết chiều cao của tháp là $%s$m và khoảng cách từ nóc tháp đến tâm đối xứng của hypebol bằng $\\dfrac{2}{3}$ lần khoảng cách từ tâm đối xứng đến đáy. '''
                                'Tính bán kính nóc và bán kính đáy của tháp.}'
                                '{'
                                '''\\scalebox{0.7}{
                                \\begin{tikzpicture}
                    \\begin{axis}[view={30}{15},
                        hide axis,
                        axis equal,
                        z buffer=sort,
                        samples=20,
                        domain=0:360,
                        y domain=-3:2,
                        ]
                        \\addplot3[
                        surf,
                        shader=flat,
                        opacity=0.4,
                        ]
                        ({cos(x)*sqrt(1+y^2)}, {sin(x)*sqrt(1+y^2)}, y);
                    \\end{axis}
                \\end{tikzpicture}
                                }'''
            '}'
                                %(latex(a), latex(b), latex(h)))

                # Nội dung lời giải
                loigiai=('Chọn hệ trục tọa độ như hình vẽ\\\\ \n'
                                '''\\begin{center}
                                \\scalebox{0.7}{
                                \\begin{tikzpicture}	[line join=round, line cap=round,>=stealth,thick] 
                    \\begin{axis}[view={30}{15},
                        hide axis,
                        axis equal,
                        z buffer=sort,
                        samples=25,
                        domain=0:360,
                        y domain=-3:2,
                        ]
                        \\addplot3[
                        surf,
                        shader=flat,
                        opacity=0.4,
                        ]
                        ({cos(x)*sqrt(1+y^2)}, {sin(x)*sqrt(1+y^2)}, y);
                    \\end{axis}
                    \\draw [->] (1,3.2) -- (6.5,3.2);
                    \\draw [->] (3.43,0) -- (3.43,6);
                    \\draw (6.2,3.19) node[anchor=north west] {$x$};
                    \\draw (3,6) node[anchor=north west] {$y$};
                    \\draw (2.8,3.2) node[anchor=north west] {$O$};
                    \\draw [dash pattern=on 1pt off 1pt,color=black] (1.95,4.5)-- (4.92,4.5);
                    \\draw [dash pattern=on 1pt off 1pt,color=black] (1.3,1.21)-- (5.55,1.21);
                    \\draw (3.35,5) node[anchor=north west] {$H$};
                    \\draw (3.35,1.7) node[anchor=north west] {$K$};
                \\end{tikzpicture}}
                \\end{center}'''
                        'Ta có $\\heva{&HK=%s \\\\& OH=\\dfrac{2}{3}OK}\\Rightarrow \\heva{&OH+OK=%s \\\\& OH=\\dfrac{2}{3}OK}\\Rightarrow OH=%s\\text{m},OK=%s\\text{m}$.\\\\ \n'
                        'Đường thẳng qua $H$, vuông góc $Oy$ là $\\Delta_1: y=%s$ cắt hypebol tại điểm có hoành độ dương và thỏa mãn '
                        '$\\dfrac{x^2}{%s^2}-\\dfrac{%s^2}{%s^2}=1\\Rightarrow x=%s$m.\\\\ \n'
                        'Đường thẳng qua $K$, vuông góc $Oy$ là $\\Delta_2: y=%s$ cắt hypebol tại điểm có hoành độ dương và thỏa mãn '
                        '$\\dfrac{x^2}{%s^2}-\\dfrac{\\left(%s\\right)^2}{%s^2}=1\\Rightarrow x=%s$m.\\\\ \n'
                        'Vậy bán kính nóc của tháp bằng $%s$m, bán kính đáy của tháp bằng $%s$m.'

                        %(latex(h),latex(h),latex(oh),latex(ok),
                        latex(oh),
                        latex(a),latex(oh),latex(b),latex(x1),
                        latex(-ok),
                        latex(a),latex(-ok),latex(b),latex(x2),
                        latex(x1),latex(x2),
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- +','-').replace('+ -', '-').replace('- -', '+')
            return content 

