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


def bt_dang1_p3_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['2']
            dang=random.choice(lisdang)

            if dang=='2':
                # Khai báo biến

                a = randint(1,15)

                x0 = sqrt((a**4)/8)

                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện đều $ABCD$ cạnh bằng $%s$, gọi $G$ là trọng tâm tam giác $ABC$$zz$'
                                ' Cắt tứ diện bởi mặt phẳng $(GCD)$ được thiết diện có diện tích bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục)$zz$\n'
                                %(latex(a)))

                # Nội dung lời giải
                loigiai = ('\\begin{center}\\scalebox{0$zz$6}{\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm]\n'
            '\\clip(-0$zz$5081130367624446,-2$zz$813258160062258) rectangle (7$zz$617096201704652,4$zz$672889677626565);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1,0)-- (6,0);\n'
            '\\draw (1,0)-- (3,-2);\n'
            '\\draw (3,-2)-- (6,0);\n'
            '\\draw (6,0)-- (3,4);\n'
            '\\draw (3,4)-- (1,0);\n'
            '\\draw (3,-2)-- (3,4);\n'
            '\\draw (3,4)-- (4$zz$5,-1$zz$);\n'
            '\\draw (3,-2)-- (4$zz$5,2$zz$);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (4$zz$5,2)-- (2,-1);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1,0)-- (4$zz$5,2);\n'
            '\\draw (2$zz$7,4$zz$5) node[anchor=north west] {$A$};\n'
            '\\draw (6,0$zz$4) node[anchor=north west] {$B$};\n'
            '\\draw (2$zz$7,-2) node[anchor=north west] {$C$};\n'
            '\\draw (0$zz$4,0$zz$2) node[anchor=north west] {$D$};\n'
            '\\draw (4,1) node[anchor=north west] {$G$};\n'
            '\\draw (4$zz$5,2$zz$6) node[anchor=north west] {$M$};\n'
            '\\draw (1$zz$5,-1) node[anchor=north west] {$N$};\n'
            '\\end{tikzpicture}} \n'
            '\\end{center}\n'
                    'Gọi $M$ là trung điểm của $AB$. Khi đó thiết diện cắt bởi $(GCD)$ là tam giác $CDM$$zz$\\\\ \n'
                    'Ta có $\\Delta CDM$ cân tại $M$ và $MD=MC=\\dfrac{%s\\sqrt{3}}{2};CD=%s$$zz$\\\\ \n'
                    'Gọi $N$ là trung điểm $CD$, tính được $MN=\\sqrt{{{\\left( \\frac{%s\\sqrt{3}}{2} \\right)}^{2}}-{{\\left( \\dfrac{%s}{2} \\right)}^{2}}}=\\dfrac{%s\\sqrt{2}}{2}$$zz$\\\\ \n'
                    'Vậy ${{S}_{\\Delta CDM}}= \\dfrac{1}{2}CD\\cdot MN= \\dfrac{\\sqrt{2}\\cdot{{%s}^{2}}}{4} \\approx %s$$zz$'
                    %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(kq))
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{\n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

