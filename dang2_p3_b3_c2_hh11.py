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


def bt_dang2_p3_b3_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                sa=randint(2,9)
                ab=randint(2,9)
                bc=randint(2,9)
                ac=sqrt(ab**2+bc**2)
                t=sa/ac
                goc=atan(t)*180/pi
                h1=goc
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $SzzABC$ có $SA$ vuông góc với mặt phẳng $\\left(ABC\\right)$, $SA=%s$, tam giác $ABC$ vuông tại $B$, $AB=%s$ và $BC=%s$zz Góc giữa đường thẳng $SC$ và mặt phẳng $\\left(ABC\\right)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)zz'''
                                %(latex(sa),latex(ab),latex(bc)
                                ))

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-0zz74,-1zz66) rectangle (4zz62,3zz94);
                    \\draw (-0zz2,3zz6) node[anchor=north west] {$S$};
                    \\draw (-0zz6,0zz46) node[anchor=north west] {$A$};
                    \\draw (0zz6,-1) node[anchor=north west] {$B$};
                    \\draw (4,0zz3) node[anchor=north west] {$C$};
                    \\draw (15zz1,1zz86) node[anchor=north west] {$D$};
                    \\draw (13zz1,1zz4) node[anchor=north west] {$H$};
                    \\draw (12zz8,-0zz72) node[anchor=north west] {$K$};
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (4zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (1zz,-1zz);
                    \\draw [line width=1zzpt] (1zz,-1zz)-- (4zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (0zz,3zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (1zz,-1zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (4zz,0zz);
                \\end{tikzpicture}
            \\end{center}
            Ta thấy hình chiếu vuông góc của $SC$ lên $\\left(ABC\\right)$ là $AC$ nên $\\left(SC,ABC\\right)=\\widehat{SCA}$zz\\\\
                    Mà $AC=\\sqrt{A{{B}^2}+B{{C}^2}}=%s$ nên $\\tan \\widehat{SCA}=\\dfrac{SA}{AC}=%s$zz\\\\
                    Vậy góc giữa đường thẳng $SC$ và mặt phẳng $\\left(ABC\\right)$ bằng ${%s^\\circ}$zz'''
                        %(latex(ac),latex(t),latex(kq)
                        ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.')
            return content                

