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


def bt_dang1_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                y=symbols('y')
                #a=60
                #b=80
                c=randint(10,35)
                a=3*c
                b=4*c
                x0=-Rational(4*c,a**2)
                y0=Rational(4*c,a)
                f=x0*x**2+y0*x
                tp=integrate(f, (x, 0, a))

                h1=a*b-2*tp

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{ \n'
                                'Kiến trúc sư thiết kế một khu sinh hoạt cộng đồng có dạng hình '
                                    'chữ nhật với chiều rộng và chiều dài lần lượt là $%s$m và $%s$m. Trong đó, '
                                    'phần được tô màu đậm là sân chơi, phần còn lại để trồng hoa. Mỗi phần '
                                    'trồng hoa có đường biên cong là một phần của parabol với đỉnh thuộc '
                                    'một trục đối xứng của hình chữ nhật và khoảng cách từ đỉnh đó đến trung '
                                    'điểm cạnh tương ứng của hình chữ nhật bằng $%s$m (xem hình minh họa). '
                                    'Tính diện tích của phần sân chơi.'
                                '}\n'
                                '{\n'
                                '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.}  \n'
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                    '\\clip(-0.6458874458874482,-0.4792207792207782) rectangle (6.644155844155837,8.47316017316017); \n'
                                    '\\draw[fill=zzttqq,fill opacity=0.1] {[smooth,samples=50,domain=0.0:6.0] plot(\\x,{0.22*(\\x-3.0)^(2.0)+6.0})} -- (6.,0.02) {[smooth,samples=50,domain=6.0:0.0] -- plot(\\x,{0-0.22*(\\x-3.0)^(2.0)+2.0})} -- (0.,7.98) -- cycle; \n'
                                    '\\draw [line width=1.pt] (0.,8.)-- (0.,0.); \n'
                                    '\\draw [line width=1.pt] (0.,0.)-- (6.,0.); \n'
                                    '\\draw [line width=1.pt] (6.,0.)-- (6.,8.); \n'
                                    '\\draw [line width=1.pt] (6.,8.)-- (0.,8.); \n'
                                    '\\draw [->,line width=1.pt] (3.,7.) -- (3.,8.); \n'
                                    '\\draw [->,line width=1.pt] (3.,7.) -- (3.,6.); \n'
                                    '\\draw [->,line width=1.pt] (3.,1.) -- (3.,2.); \n'
                                    '\\draw [->,line width=1.pt] (3.,1.) -- (3.,0.); \n'
                                    '\\draw (3.1982683982683935,7.503463203463201) node[anchor=north west] {$%s m$}; \n'
                                    '\\draw (3.1809523809523763,1.390909090909091) node[anchor=north west] {$%s m$}; \n'
                                '\\end{tikzpicture} } \n'
                                '}\n'
                                %(latex(a),latex(b),latex(c),
                                latex(c),latex(c)
                                ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                    '\\scalebox{0.6}{  \n'
                        '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-1.3385281385281405,-1.587445887445886) rectangle (7.752380952380944,9.546753246753244); \n'
                            '\\draw[fill=zzttqq,fill opacity=0.1] {[smooth,samples=50,domain=0.0:6.0] plot(\\x,{0.22*(\\x-3.0)^(2.0)+6.0})} -- (6.,0.02) {[smooth,samples=50,domain=6.0:0.0] -- plot(\\x,{0-0.22*(\\x-3.0)^(2.0)+2.0})} -- (0.,7.98) -- cycle; \n'
                            '\\draw [line width=1.pt] (0.,8.)-- (0.,0.); \n'
                            '\\draw [line width=1.pt] (0.,0.)-- (6.,0.); \n'
                            '\\draw [line width=1.pt] (6.,0.)-- (6.,8.); \n'
                            '\\draw [line width=1.pt] (6.,8.)-- (0.,8.); \n'
                            '\\draw [->,line width=1.pt] (3.,7.) -- (3.,8.); \n'
                            '\\draw [->,line width=1.pt] (3.,7.) -- (3.,6.); \n'
                            '\\draw [->,line width=1.pt] (3.,1.) -- (3.,2.); \n'
                            '\\draw [->,line width=1.pt] (3.,1.) -- (3.,0.); \n'
                            '\\draw (3.1982683982683935,7.503463203463201) node[anchor=north west] {$%s m$}; \n'
                            '\\draw (3.1809523809523763,1.390909090909091) node[anchor=north west] {$%s m$}; \n'
                            '\\draw [->,line width=1.pt] (-1.0095238095238115,0.) -- (7.163636363636357,0.); \n'
                            '\\draw [->,line width=1.pt] (0.,-0.9987012987012975) -- (0.,9.11385281385281); \n'
                            '\\draw (-0.5766233766233789,0) node[anchor=north west] {$O$}; \n'
                            '\\draw (6.661471861471854,0) node[anchor=north west] {$x$}; \n'
                            '\\draw (-0.5766233766233789,9.200432900432897) node[anchor=north west] {$y$}; \n'
                            '\\draw (2.6787878787878747,0) node[anchor=north west] {$%s$}; \n'
                            '\\draw (5.622510822510816,0.05757575757575834) node[anchor=north west] {$%s$}; \n'
                            '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (3.,2.)-- (0.,2.0142857142857142); \n'
                            '\\draw (-0.6978354978355,2.5337662337662334) node[anchor=north west] {$%s$}; \n'
                    '\\end{tikzpicture} }  \n'
                '\\end{center}  \n'
                            'Diện tích của phần sân chơi bằng diện tích của hình chữ nhật trừ đi diện tích của hai phần trồng hoa. \\\\ \n'
                        'Diện tích của hình chữ nhật là $S=%s \\cdot %s = %s$m$^2$. \\\\ \n'
                        'Gắn hệ trục tọa độ như hình vẽ. \\\\ \n'
                        'Diện tích của mỗi phần trồng hoa là diện tích hình phẳng giới hạn bởi một parabol với trục $Ox$.\\\\ \n'
                        'Parabol có dạng $y=ax^2+bx+c$. \\\\ \n'
                        'Parabol đi qua ba điểm $(0;0), (%s;0)$ và $\\left(%s;%s \\right)$ nên ta có hệ phương trình \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& c=0 \\\\& %sa+%sb+c=0 \\\\& %s a+%sb+c=%s} \\Leftrightarrow \\heva{& a=%s \\\\& b=%s \\\\& c=0.}$ \\\\ \n'
                        'Suy ra $y=%sx^2+%sx$. \\\\ \n'
                        'Diện tích hình phẳng giới hạn bởi parabol và trục $Ox$ là \\\\ \n'
                        '\\hspace*{1cm} $S_1=\\displaystyle \\int\\limits_{0}^{%s}{\\left( %sx^2+%sx \\right)} \\text{d}x=%s$m$^2$. \\\\ \n'
                        'Vậy diện tích phần sân chơi là \\\\ \n'
                        '\\hspace*{1cm} $S_2=S-2S_1=%s-2\\cdot %s=%s$m$^2$.'

                        %(latex(c),latex(c),
                            latex(Rational(a,2)),
                            latex(a),
                            latex(c),

                            latex(a),latex(b),latex(a*b),
                            latex(c),latex(Rational(a,2)),latex(c),
                            latex(a**2),latex(a),latex(Rational(a**2,4)),latex(Rational(a,2)),latex(c),latex(x0),latex(y0),
                            latex(x0),latex(y0),
                            latex(a),latex(x0),latex(y0),latex(tp),
                            latex(a*b),latex(tp),latex(a*b-2*tp)
                            ))

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

