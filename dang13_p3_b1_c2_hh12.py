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


def bt_dang13_p3_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x,y,z=symbols('x y z')
                a=randint(-5,5)
                b=a+1 
                c=randint(-5,5)
                d=randint(-9,9)
                p=a*x+b*y+c*z+d

                xa=randint(-5,5)
                ya=randint(-5,5)
                za=randint(-5,5)

                k=randint(2,5)

                kca=(abs(a*xa+b*ya+c*za+d))/(sqrt(a**2+b**2+c**2))
                number = Decimal(float((k-1)*kca))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(P): %s=0$ và điểm $A(%s;%s;%s)$. Lấy một điểm $M$ trên $(P)$, gọi $B$ là điểm sao cho $\\vec{AB}=%s \\vec{AM}$. Khoảng cách từ $B$ đến mặt phẳng $(P)$ bằng bao nhiêu? (làm tròn đến hàng đơn vị).'''
                                %(latex(p),latex(xa),latex(ya),latex(za),latex(k)
                                ))
                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-0.2541487331816513,-1.68333230816919) rectangle (6.167578383943014,2.2410564856292154);
                    \\draw [line width=1.pt] (0.,0.)-- (2.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                    \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                    \\draw [line width=1.pt] (2.240554471372508,1.6921220244479762)-- (3.0357830297178907,0.6434143631300033);
                    \\draw [line width=1.pt,dashed] (3.0357830297178907,0.6434143631300033)-- (3.5236801771150494,0.);
                    \\draw [line width=1.pt] (3.5236801771150494,0.)-- (4.417530666956299,-1.178765333478148);
                    \\draw [line width=1.pt] (2.240554471372508,1.6921220244479762)-- (2.281372775039704,0.6308461291008782);
                    \\draw [line width=1.pt] (2.281372775039704,0.6308461291008782)-- (4.403924565733901,0.6172400278784795);
                    \\draw [line width=1.pt,dashed] (4.403924565733901,0.6172400278784795)-- (4.407058737394364,0.20352936869718236);
                    \\draw [line width=1.pt] (4.407058737394364,0.20352936869718236)-- (4.417530666956299,-1.178765333478148);
                    \\draw [line width=1.pt] (2.,1.)-- (2.2671745492358917,1.);
                    \\draw [line width=1.pt] (2.76538633825249,1.)-- (6.,1.);
                    \\draw [line width=1.pt,dashed] (2.2671745492358917,1.)-- (2.76538633825249,1.);
                    \\draw [shift={(0.5933368654053285,0.06923669864490693)},line width=1.pt]  plot[domain=-0.2568795049219572:1.3063628899074626,variable=\\t]({1.*0.2725170946564988*cos(\\t r)+0.*0.2725170946564988*sin(\\t r)},{0.*0.2725170946564988*cos(\\t r)+1.*0.2725170946564988*sin(\\t r)});
                    \\draw (0.3,0.4368569622465719) node[anchor=north west] {$P$};
                    \\draw (1.9,2.200283615044297) node[anchor=north west] {$A$};
                    \\draw (2.6,0.7018806210485421) node[anchor=north west] {$M$};
                    \\draw (4.261446684098074,-1.1023189023341013) node[anchor=north west] {$B$};
                    \\draw (1.8,0.7732331445721495) node[anchor=north west] {$H$};
                    \\draw (4.4551178193764365,0.9567110622042827) node[anchor=north west] {$K$};
                \\end{tikzpicture}
            \\end{center}
            Vì $\\vec{AB}=%s \\vec{AM}$ nên điểm $B$ nằm khác phía với điểm $A$ so với mặt phẳng $(P)$ và $BM=%s AM$. \\\\
                Do đó khoảng cách từ $B$ đến mặt phẳng (P) sẽ gấp $%s$ khoảng cách từ $A$ đến mặt phẳng $(P)$. \\\\
                    Ta có \\\\
                        $d\\left(A,(P) \\right)=\\frac{\\left| %s \\cdot (%s)+%s \\cdot (%s)+%s \\cdot (%s)+%s\\right|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$.\\\\
                            Vậy $d\\left(B,(P) \\right)=%s d\\left(A,(P) \\right)=%s \\cdot %s=%s \\approx %s$.'''
                        %(latex(k),latex(k-1),
                        latex(k-1),
                        latex(a),latex(xa),latex(b),latex(ya),latex(c),latex(za),latex(d),
                        latex(a),latex(b),latex(c),latex(kca),
                        latex(k-1),
                        latex(k-1),latex(kca),latex((k-1)*kca),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content  

