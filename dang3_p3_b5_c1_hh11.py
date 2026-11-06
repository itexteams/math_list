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


def bt_dang3_p3_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,9)
                h1=1/a  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình lăng trụ $ABC$zz$A\'B\'C\'$, gọi $I$ là điểm thuộc $AB$ sao cho $AI=\\dfrac{1}{%s} AB$$zz$ Gọi $S, S\'$ lần lượt là diện tích của tam giác $\\Delta ABC$ và hình chiếu của tam giác $AA\'C\'$ lên mặt phẳng $(A\'B\'C\')$ theo phương $IB\'$$zz$ Khi đó tỉ số $\\dfrac{S\'}{S}$ bằng bao nhiêu?  \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

            '\\begin{center} \n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm] \n'
                    '\\clip(-1$zz$078951674312687,-2$zz$5045860513518257) rectangle (5$zz$790779789116996,4$zz$704256360113406); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw (0$zz$,0$zz$)-- (1$zz$,-2$zz$); \n'
                    '\\draw (1$zz$,-2$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw (0$zz$,0$zz$)-- (1$zz$,4$zz$); \n'
                    '\\draw (1$zz$,4$zz$)-- (5$zz$,4$zz$); \n'
                    '\\draw (5$zz$,4$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw (1$zz$,4$zz$)-- (2$zz$,2$zz$); \n'
                    '\\draw (2$zz$,2$zz$)-- (1$zz$,-2$zz$); \n'
                    '\\draw (2$zz$,2$zz$)-- (5$zz$,4$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,0$zz$)-- (1$zz$,-2$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,0$zz$)-- (1$zz$,4$zz$); \n'
                    '\\draw (1$zz$,4$zz$)-- (1$zz$,-2$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,4$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw (0$zz$61,4$zz$5) node[anchor=north west] {$A$}; \n'
                    '\\draw (4$zz$9,4$zz$5) node[anchor=north west] {$B$}; \n'
                    '\\draw (2,2$zz$1) node[anchor=north west] {$C$}; \n'
                    '\\draw (2$zz$7,4$zz$5) node[anchor=north west] {$I$}; \n'
                    '\\draw (-0$zz$6,0$zz$3) node[anchor=north west] {$A\'$}; \n'
                    '\\draw (4,0$zz$2) node[anchor=north west] {$B\'$}; \n'
                    '\\draw (0$zz$71,-2) node[anchor=north west] {$C\'$}; \n'
                    '\\draw (1$zz$9,0$zz$5) node[anchor=north west] {$I\'$}; \n'
                '\\end{tikzpicture} \n'
            '\\end{center} \n'

                            'Lấy $I\'$ là điểm thuộc $A\'B\'$ sao cho $A\'I\'=\\dfrac{1}{%s} A\'B\'$$zz$ Ta có hệ thức \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& AI // I\'B\' \\\\ & AI = I\'B\' = \\dfrac{1}{%s}AB$zz$}$ \\\\ \n'
                            'Do đó, tứ giác $AIB\'I\'$ là hình bình hành$zz$ \\\\ \n'
                            'Suy ra $AI\' // IB\'$, tức là hình chiếu song song của $A$ lên mặt phẳng $(A\'B\'C\')$ theo phương $IB\'$ là $I\'$$zz$ \\\\ \n'
                            'Vậy hình chiếu của $\\Delta AA\'C\'$ lên mặt phẳng $(A\'B\'C\')$ theo phương $IB\'$ là $\\Delta I\'A\'C\'$$zz$ \\\\ \n'
                            'Vì $I\'$ là trung điểm $A\'B\'$ nên \\\\ \n'
                            '\\hspace*{1cm} $S\'=S_{\\Delta I\'A\'C\'}=\\dfrac{1}{%s} S_{\\Delta A\'B\'C\'}=\\dfrac{1}{%s} S_{\\Delta ABC}=\\dfrac{1}{%s} S$$zz$ \\\\ \n'
                            'Do đó $\\dfrac{S\'}{S}=\\dfrac{1}{%s}=%s$$zz$'

                        %(latex(a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(kq)
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

