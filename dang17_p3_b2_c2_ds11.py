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


def bt_dang17_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # ----------------------------------------------------
                # B1. Định nghĩa và random các tham số
                # ----------------------------------------------------
                # Chiều cao cây thấp nhất (aabb) (cm) - Random từ 90 đến 120
                min_height = random.randint(90, 120) 
                # Chiều cao tăng thêm khi có thêm 1 alen trội (cm) - Random từ 3 đến 7
                inc_height = random.randint(3, 7)

                # Danh sách các kiểu gen có thể hỏi và số alen trội tương ứng
                # (Kiểu gen, Số alen trội)
                genotypes = [
                    ('AABB', 4), ('AABb', 3), ('AaBB', 3), 
                    ('AaBb', 2), ('AAbb', 2), ('aaBB', 2), 
                    ('Aabb', 1), ('aaBb', 1),
                ]

                # Chọn ngẫu nhiên kiểu gen và số alen trội để hỏi
                (gen_to_ask, dominant_alleles) = random.choice(genotypes)

                # Tính toán kết quả
                # Chiều cao = Chiều cao thấp nhất + Số alen trội * Mức tăng
                height_to_ask = min_height + dominant_alleles * inc_height

                kq = str(height_to_ask) 

                # Chuẩn bị đáp án trắc nghiệm
                da = '$%s \\text{ (cm)}$'%(kq) # Đáp án đúng

                # Tạo các đáp án sai 
                kq_num = height_to_ask

                s = ['$%s \\text{ (cm)}$'%(kq_num + inc_height), # Tính nhầm +1 alen trội
                     '$%s \\text{ (cm)}$'%(kq_num - inc_height), # Tính nhầm -1 alen trội
                     '$%s \\text{ (cm)}$'%(min_height + 4 * inc_height), # Chiều cao cây cao nhất AABB (nếu khác gen_to_ask)
                     '$%s \\text{ (cm)}$'%(min_height), # Chiều cao cây thấp nhất
                     '$%s \\text{ (cm)}$'%(kq_num + 10) if kq_num + 10 != min_height + 4 * inc_height else '$$%s \\text{ (cm)}$$'%(kq_num - 10)
                    ]

                # Loại bỏ các đáp án trùng và đảm bảo có đủ 3 đáp án sai
                s = list(set(s))
                while len(s) > 3:
                    s.pop(random.randrange(len(s))) # Bỏ bớt nếu có quá nhiều
                while len(s) < 3: # Thêm vào nếu không đủ
                    s.append('$$%s \\text{ (cm)}$$'%(random.choice([kq_num + 5, kq_num - 5, kq_num + 15, kq_num - 15])))
                    s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # ----------------------------------------------------
                # B2. Tạo nội dung câu hỏi và lời giải
                # ----------------------------------------------------
                # Câu hỏi
                noidungcauhoi = ('''Ở một loài thực vật lưỡng bội, tính trạng chiều cao cây do hai gene không alen là $A$ và $B$ cùng quy định theo kiểu tương tác cộng gộp. Trong kiểu gene cứ thêm một alen trội $A$ hay $B$ thì chiều cao cây tăng thêm $%s$ cm. Khi trưởng thành, cây thấp nhất của loài này với kiểu gene $aabb$ có chiều cao $%s$ cm. Hỏi cây với kiểu gene $%s$ có chiều cao bao nhiêu?'''
                                  %(inc_height, min_height, gen_to_ask))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Tính trạng chiều cao được quy định bởi tương tác cộng gộp. \\\\
                         Cây thấp nhất ($aabb$) có 0 alen trội $\\rightarrow h_{min} = %s \\text{ cm}$. \\\\
                         Mỗi alen trội làm tăng chiều cao $\\Delta h = %s \\text{ cm}$.\\\\
                         Kiểu gene $%s$ có $%s$ alen trội. \\\\
                         $\\text{Chiều cao} = h_{min} + (\\text{Số alen trội} \\cdot \\Delta h)$ \\\\
                         $\\text{Chiều cao}_{%s} = %s + (%s \\cdot %s) = %s + %s = %s \\text{ (cm.)}$'''
                          %(min_height, inc_height,
                            gen_to_ask, dominant_alleles,
                            gen_to_ask, min_height, dominant_alleles, inc_height, min_height, dominant_alleles * inc_height, height_to_ask
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(height_to_ask)


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

