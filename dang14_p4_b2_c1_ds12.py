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


def bt_dang14_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(3,6)
                b=randint(1,2)
                c=randint(200,600)
                f=x**3-(2*a+b)*x**2+(a*a+a*b)*x
                daoham=3*x**2-2*(2*a+b)*x+a*a+a*b
                delta=(2*a+b)**2-3*(a*a+a*b)
                x1=(2*a+b-sqrt(delta))/3
                x2=(2*a+b+sqrt(delta))/3
                f1=x1**3-(2*a+b)*x1**2+(a*a+a*b)*x1
                thamso=round(c/(1000*f1),2)
                f2=x2**3-(2*a+b)*x2**2+(a*a+a*b)*x2
                y2=(c/(1000*f1))*f2
                number = Decimal(float(y2))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini { Lát cắt của một vùng đất ven biển được mô hình hóa thành một hàm số bậc ba $y=f(x)$ có đồ thị như hình vẽ (đơn vị độ dài trên các trục là km)$zz$ Biết khoảng cách hai bên chân đồi $OA$ là $%s$ km, độ rộng của hồ $AB$ là $%s$ km và ngọn đồi cao $%s$ m$zz$ Độ sâu của hồ (tính bằng ki-lô-mét) tại điểm sâu nhất bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm)$zz$ } \n'
                                '{ \n'
                                '\\scalebox{1}{  \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]    \n'
                                '\\draw[->] (-0$zz$5,0)--(5,0) node[below left] {$x$};     \n'
                                '\\draw[->] (0,-1)--(0,4) node[below left] {$y$};    \n'
                                '\\clip(-1$zz$364490336909125,-1$zz$4093710655554836) rectangle (5$zz$842723400033483,3$zz$9006336090149425); \n'
                                '\\draw[fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=0$zz$0:2$zz$3] plot(\\x,{(\\x-0$zz$9)^(3$zz$0)-3$zz$0*(\\x-0$zz$9)^(2$zz$0)+3$zz$0}) -- (2$zz$3,0$zz$) -- (0$zz$,0$zz$) -- cycle; \n'
                                '\\draw[dash pattern=on 1pt off 1pt,fill=black,pattern=dots,pattern color=black, smooth,samples=50,domain=2$zz$3:3$zz$5] plot(\\x,{(\\x-0$zz$9)^(3$zz$0)-3$zz$0*(\\x-0$zz$9)^(2$zz$0)+3$zz$0}) -- (3$zz$5,0$zz$) -- (2$zz$3,0$zz$) -- cycle; \n'
                                '\\draw[fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=3$zz$5:4$zz$0] plot(\\x,{(\\x-0$zz$9)^(3$zz$0)-3$zz$0*(\\x-0$zz$9)^(2$zz$0)+3$zz$0}) -- (4$zz$,0$zz$) -- (3$zz$5,0$zz$) -- cycle; \n'
                                '\\draw[line width=1$zz$pt,smooth,samples=100,domain=0:5$zz$842723400033483] plot(\\x,{((\\x)-0$zz$9)^(3$zz$0)-3$zz$0*((\\x)-0$zz$9)^(2$zz$0)+3$zz$0}); \n'
                                '\\draw (-0$zz$5249208093076413,0$zz$7168115043443789) node[anchor=north west] {$O$}; \n'
                                '\\draw (1$zz$7757177663275936,0$zz$07350498319518972) node[anchor=north west] {$A$}; \n'
                                '\\draw (3$zz$3131113168705704,0$zz$08440848355365055) node[anchor=north west] {$B$}; \n'
                                '\\draw (0$zz$5,0) node[anchor=north west] {Đồi}; \n'
                                '\\draw (4,1$zz$163855019041273) node[anchor=north west] {Núi}; \n'
                                '\\draw (2$zz$4,0$zz$6) node[anchor=north west] {Hồ}; \n'
                                '\\end{tikzpicture}} \n'
                                '} \n'
                                %(latex(a),latex(b),latex(c)
                                ))

                # Nội dung lời giải
                loigiai = ('Theo đề bài ta có $OA=%s$ km, $OB=%s$ km và $%s$ m $=%s$ km$zz$ \\\\ \n'
                        'Đồ thị hàm số $y=f(x)$ đi qua các điểm $O(0;0), A(%s;0), C(%s;0)$ suy ra \\\\ \n'
                        '$y=f(x)=ax(x-%s)(x-%s)=a(%s)$ với $a>0$$zz$ \\\\ \n'
                        'Ta có $y\'=a(%s)$; $y\'=0 \\Leftrightarrow \\hoac{& x=%s \\\\ & x=%s$zz$}$ \\\\ \n'
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5] \n'
                        '{$x$/0$zz$7,$y\'$/0$zz$7,$y$/2$zz$1} \n'
                        '{$-\\infty$,$x_{\\text{CĐ}}$,$x_{\\text{CT}}$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$y_{\\text{CĐ}}$,-/$y_{\\text{CT}}$,+/$+\\infty$} \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ độ cao trên đồi ta có tại vị trí điểm cực đại $x_{\\text{CĐ}}=%s$ và $y_{\\text{CĐ}}=%s$ suy ra \\\\ \n'
                        '$a=\\dfrac{%s}{\\left(%s\\right)^3+%s \\left(%s\\right)^2+%s \\left(%s\\right)} \\approx %s$ \\\\ \n'
                        'Điểm sâu nhất của hồ ứng với vị trí của điểm cực tiểu $x_{\\text{CT}}=%s$ và $y_{\\text{CT}}=%s$$zz$ \\\\ \n'
                        'Vậy độ sâu của hồ tại điểm sâu nhất xấp xỉ $%s$ km$zz$'


                        %(latex(a),latex(a+b),latex(c),latex(c/1000),
                            latex(a),latex(a+b),
                            latex(a),latex(a+b),latex(f),
                            latex(daoham),latex(x1),latex(x2),
                            latex(x1),latex(c/1000),
                            latex(c/1000),latex(x1),latex(-(2*a+b)),latex(x1),latex((a*a+a*b)),latex(x1),latex(thamso),
                            latex(x2),latex(y2),
                            latex(abs(kq))
                            ))

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.', ',').replace('$zz$', '.')
            return content

