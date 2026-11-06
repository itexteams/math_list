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


def bt_dang5_p3_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,8)
                pa=a/10
                p_a=1-pa

                pm=pa+p_a*0.5
                pn=pm

                kq=pm*pn

                h1=kq   
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Câu hỏi
                noidungcauhoi = ('Hình dạng của hạt đậu Hà Lan có hai kiểu hình: Hạt trơn và hạt nhăn, có hai gene ứng với hai kiểu hình này là gene trội $B$ và gene lặn $b$. Khi cho hai cây đậu Hà Lan, cây con lấy ngẫu nhiên một cách độc lập một gene từ cây bố và một gene từ cây mẹ để hình thành một cặp gene. Giả sử cây bố và cây mẹ được chọn ngẫu nhiên từ một quần thể các cây đậu Hà Lan, ở đó tỉ lệ cây mang kiểu gene $bb, Bb$ tương ứng là $%s$ và $%s$. Xác suất để cây con có kiểu gene $bb$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)zz'
                                %(latex(pa),latex(p_a)
                                ))

                # Nội dung lời giải
                loigiai=('Gọi các biến cố: \\\\ \n'
                        '\\hspace*{1cm} $A$:"Cây bố có kiểu gene $bb$"zz \\\\ \n'
                        '\\hspace*{1cm} $M$:"Cây con lấy gene $b$ từ cây bố"zz \\\\ \n'
                        '\\hspace*{1cm} $N$:"Cây con lấy gene $b$ từ cây mẹ"zz \\\\ \n'
                        '\\hspace*{1cm} $E$:"Cây con có kiểu gene $bb$"zz \\\\ \n'
                        'Theo giả thiết $M$ và $N$ độc lập nên $P(E)=P(M) \\cdot P(N)$zz \\\\ \n'
                        'Tính $P(M)$zz Theo công thức xác suất toàn phần, ta có \n'           
                        '$$P(M)=P(A) \\cdot P(M | A) +P(\\overline{A}) \\cdot P(M | \\overline{A})zz \\hspace*{1cm} (*)$$ \n'
                        'Ta có $P(A)=%s$; $P(\\overline{A})=%s$zz \\\\ \n'
                        '$P(M|A)$ là xác suất của cây con lấy gene $b$ từ cây bố với điều kiện cây bố có kiểu gene $bb$zz Do đó $P(M|A)=1$zz \\\\ \n'
                        '$P(M| \\overline{A})$ là xác suất của cây con lấy gene $b$ từ cây bố với điều kiện cây bố có kiểu gene $Bb$zz Do đó $P(M| \\overline{A})=0.5$zz \\\\ \n'
                        'Thay vào (*) ta được $P(M)=%s \\cdot 1+%s \\cdot 0.5=%s$zz \\\\ \n'
                        'Tương tự ta tính được $P(N)=%s$zz \\\\ \n'
                        'Suy ra $P(E)=P(M) \\cdot P(N)=%s \\cdot %s =%s$zz \\\\ \n'
                        'Vậy tỉ lệ cây con có kiểu gene $bb$ là khoảng $%s$zz'
                        %(latex(pa),latex(p_a),
                        latex(pa),latex(p_a),latex(pm),
                        latex(pn),
                        latex(pm),latex(pn),latex(kq),
                        latex(kq)
                        ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kqz))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content    

