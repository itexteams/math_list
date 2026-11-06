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


def bt_dang2_p4_b3_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                sa=randint(2,5)
                ab=randint(3,6)
                bc=randint(3,6)
                ac=sqrt(ab**2+bc**2)
                tang=sa/ac
                goc=atan(tang)
                goc1=goc*180/pi
                h1=goc1
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA \\bot (ABC)$, tam giác $ABC$ vuông tại $B$, $SA=%s$, $AB=%s$ và $BC=%s$zz \\\\
                                a) Tìm hình chiếu vuông góc của $A$ trên mặt phẳng $(SBC)$zz \\\\
                                b) Tính góc giữa $SC$ với mặt phẳng $(ABC)$zz'''
                                %(latex(sa),latex(ab),latex(bc)
                                ))

                # Nội dung lời giải
                loigiai = (    '''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-0zz8108,-1zz6442) rectangle (5zz6692,4zz8958);
                    \\draw [line width=1zzpt,dash pattern=on 4pt off 4pt] (0zz,0zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (2zz,-1zz);
                    \\draw [line width=1zzpt] (2zz,-1zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (0zz,4zz);
                    \\draw [line width=1zzpt] (0zz,4zz)-- (2zz,-1zz);
                    \\draw [line width=1zzpt] (0zz,4zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (0zz9944413793103448,1zz5138965517241378);
                    \\draw (-0zz2,4zz6) node[anchor=north west] {$S$};
                    \\draw (-0zz7,0zz3) node[anchor=north west] {$A$};
                    \\draw (1zz7892,-0zz9) node[anchor=north west] {$B$};
                    \\draw (5zz0692,0zz4) node[anchor=north west] {$C$};
                    \\draw (0zz9,2zz1) node[anchor=north west] {$H$};
                \\end{tikzpicture}
            \\end{center}
            \\begin{enumEX}[a)]{1}
                                \\item  Gọi $H$ là chân đường cao dựng từ đỉnh $A$ đến cạnh $SB$zz \\\\
                                    Ta có $AH \\bot SB$zz \\\\
                                    Theo giả thiết $SA \\bot (ABC)$ nên $SA \\bot BC$ và tam giác $ABC$ vuông tại $B$zz \\\\
                                    Suy ra $\\heva{& BC \\bot SA \\\\& BC \\bot AB} \\Rightarrow BC \\bot (SAB) \\Rightarrow BC \\bot AH$zz \\\\
                                    Ta có $\\heva{& AH \\bot SB \\\\& AH \\bot BC} \\Rightarrow AH \\bot (SBC)$zz \\\\
                                    Vậy $H$ là hình chiếu vuông góc của $A$ trên mặt phẳng $(SBC)$zz
                                \\item  Xét tam giác $ABC$ vuông tại $B$ ta có \\\\
                                    $AC=\\sqrt{AB^2+BC^2}=\\sqrt{%s^2+%s^2}=%s$zz \\\\
                                    Đường thẳng $SC$ có hình chiếu vuông góc trên mặt phẳng $(ABC)$ là $AC$ nên góc giữa $SC$ và $(ABC)$ là góc $\\widehat{SCA}$zz \\\\
                                    Xét tam giác $SAC$ vuông tại $A$, ta có \\\\
                                    $\\tan \\widehat{SCA}=\\frac{SA}{AC} =%s \\Rightarrow \\widehat{SCA} \\approx %s^\\circ$zz \\\\
                                    Suy ra góc giữa đường thẳng $SC$ và mặt phẳng $(ABC)$ bằng $%s^\\circ$zz
                                \\end{enumEX} \n'''

                        %(latex(ab),latex(bc),latex(ac),
                            latex(tang),latex(kq),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.')
            return content  

