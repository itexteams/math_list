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


def bt_dang1_p3_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,9)
                h1=1-Rational(a+1,2*a)   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp $S$zz$ABCD$ có đáy là hình bình hành, trên cạnh $SA$ lấy điểm $M$ sao cho $MA = %sMS$$zz$ Gọi $O$ là tâm của hình bình hành $ABCD$$zz$ Một phép chiếu song song theo phương $MO$ lên mặt phẳng $(ABCD)$ biến điểm $S$ thành điểm $N$$zz$ Tỉ số $\\dfrac{CN}{CA}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm)$zz$  \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                            '\\begin{center}  \n'
                                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm] \n'
                                    '\\clip(-0$zz$820849805843452,-0$zz$9805755883370291) rectangle (6$zz$947108464485262,6$zz$056558079927371); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (2$zz$,2$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (6$zz$,2$zz$); \n'
                                    '\\draw (6$zz$,2$zz$)-- (4$zz$,0$zz$); \n'
                                    '\\draw (4$zz$,0$zz$)-- (0$zz$,0$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (4$zz$,0$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (6$zz$,2$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,1$zz$)-- (3$zz$,5$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,5$zz$)-- (2$zz$,2$zz$); \n'
                                    '\\draw (3$zz$,5$zz$)-- (0$zz$,0$zz$); \n'
                                    '\\draw (3$zz$,5$zz$)-- (4$zz$,0$zz$); \n'
                                    '\\draw (3$zz$,5$zz$)-- (6$zz$,2$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,5$zz$)-- (4$zz$518971975212203,1$zz$506323991737401); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,1$zz$)-- (2$zz$0147762820930746,3$zz$357960470155124); \n'
                                    '\\draw (2$zz$8,5$zz$5) node[anchor=north west] {S}; \n'
                                    '\\draw (-0$zz$5,0) node[anchor=north west] {A}; \n'
                                    '\\draw (1$zz$4,2$zz$31) node[anchor=north west] {B}; \n'
                                    '\\draw (5$zz$9,2$zz$21) node[anchor=north west] {C}; \n'
                                    '\\draw (4,0) node[anchor=north west] {D}; \n'
                                    '\\draw (2$zz$6,1) node[anchor=north west] {O}; \n'
                                    '\\draw (1$zz$4,3$zz$7) node[anchor=north west] {M}; \n'
                                    '\\draw (4$zz$495309799495319,1$zz$6) node[anchor=north west] {N}; \n'
                                '\\end{tikzpicture}  \n'
                            '\\end{center}  \n'

                        'Trong mặt phẳng $(SAC)$ kẻ $SN$ song song với $OM$ với $N$ thuộc $AC$$zz$ Khi đó $N$ thuộc $(ABCD)$ nên $N$ là hình chiếu song song của $S$ lên mặt phẳng $(ABCD)$ theo phương $OM$$zz$ \\\\ \n'
                        'Xét $\\Delta ASN$ ta có $\\dfrac{OM}{SN} = \\dfrac{AM}{AS} = \\dfrac{AO}{AN} = \\dfrac{%s}{%s}$ (định lí Thales)$zz$ \\\\ \n'
                        'Từ đó suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\dfrac{1}{2}AC = \\dfrac{%s}{%s}AN \\Rightarrow \\dfrac{AC}{AN} = \\dfrac{%s}{%s} \\Rightarrow \\dfrac{AN}{AC} = \\dfrac{%s}{%s} \\Rightarrow \\dfrac{CN}{CA} = 1 - \\dfrac{AN}{AC} = 1 - \\dfrac{%s}{%s} = %s = %s$$zz$'
                        %(latex(a),latex(a+1),
                            latex(a),latex(a+1),latex(2*a),latex(a+1),latex(a+1),latex(2*a),latex(a+1),latex(2*a),latex(1-Rational(a+1,2*a)),latex(kq)
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

