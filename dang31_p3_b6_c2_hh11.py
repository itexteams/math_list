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


def bt_dang31_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random số liệu
                k = random.choice([2, 3, 5, 6, 7, 8, 10]) 
                q = random.choice([2, 3, 4, 5, 6])

                # Tính toán các giá trị số thực và làm tròn 1 chữ số thập phân
                val_ad_cd_num = round(math.sqrt(k), 1)
                val_q_num = float(q)

                # Diện tích đáy: S = (2*sqrt(k) + sqrt(k)) * sqrt(k) / 2 = 3k/2
                # Ở đây ta tính theo giá trị chính xác trước khi làm tròn để tránh sai số tích lũy
                dt_day_num = round(3 * k / 2, 1)
                the_tich_num = round(dt_day_num * val_q_num, 1)

                # Định dạng hiển thị số (Thay . thành ,)
                val_ad_cd = str(val_ad_cd_num).replace('.', ',')
                val_q_str = str(val_q_num).replace('.', ',')
                val_dt_day = str(dt_day_num).replace('.', ',')
                val_the_tich = str(the_tich_num).replace('.', ',')

                # Đáp án đúng (loại bỏ a^3)
                da_dung = '$%s$' % val_the_tich

                # Bước 2: Tạo các đáp án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo các biến thể sai dựa trên kết quả đúng
                    sai_val = random.choice([
                        the_tich_num * 2, 
                        the_tich_num + 2.5, 
                        the_tich_num / 2, 
                        the_tich_num + 1.2,
                        the_tich_num - 1.5
                    ])
                    sai_val = round(float(sai_val), 1)
                    if sai_val <= 0: sai_val = the_tich_num + 3.1

                    sai_str = '$%s$' % str(sai_val).replace('.', ',')
                    if sai_str != da_dung:
                        s.add(sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi (Loại bỏ ký hiệu a)
                noidungcauhoi = ('''Cho hình lăng trụ đứng $ABCD.A'B'C'D'$, đáy là hình thang vuông tại $A$ và $D$, có $AB = 2CD, AD = CD = %s, AA' = %s$. Thể tích khối lăng trụ đã cho bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).'''
                                 %(val_ad_cd, val_q_str))

                # Bước 3: Vẽ hình TikZ (Loại bỏ a trong nhãn)
                hinh_ve = '''\\begin{center}
            \\begin{tikzpicture}[line join=round, line cap=round, font=\\footnotesize, scale=0.8, line width=1pt]
                \\coordinate (D) at (0,0);
                \\coordinate (C) at (2.5,0);
                \\coordinate (A) at (1.2,1.3);
                \\coordinate (B) at (6.2,1.3);
                \\coordinate (D1) at (0,4);
                \\coordinate (C1) at (2.5,4);
                \\coordinate (A1) at (1.2,5.3);
                \\coordinate (B1) at (6.2,5.3);
                \\draw (D1)--(C1)--(B1)--(A1)--cycle;
                \\draw (D1)--(D)--(C)--(C1);
                \\draw (B1)--(B)--(C);
                \\draw[dashed] (A1)--(A)--(D);
                \\draw[dashed] (A)--(B);
                \\node[left] at (D) {$D$}; \\node[right] at (C) {$C$};
                \\node[above left] at (A) {$A$}; \\node[right] at (B) {$B$};
                \\node[left] at (D1) {$D'$}; \\node[right] at (C1) {$C'$};
                \\node[above] at (A1) {$A'$}; \\node[right] at (B1) {$B'$};
                \\node[left] at (0.6, 0.65) {$%s$};
                \\node[below] at (1.25, 0) {$%s$};
                \\node[left] at (1.2, 3.3) {$%s$};
                \\draw (0.3,0)--(0.3,0.3)--(0,0.3);
                \\draw[dashed] (1.2,1.6)--(1.5,1.6)--(1.5,1.3);
            \\end{tikzpicture}
            \\end{center}''' % (val_ad_cd, val_ad_cd, val_q_str)

                # Bước 4: Nội dung lời giải chi tiết (Loại bỏ a)
                loigiai = ('''Diện tích hình thang $ABCD$ là:
                $$S_{ABCD} = \\frac{(AB + CD) \\cdot AD}{2} = \\frac{(2CD + CD) \\cdot AD}{2} = \\frac{3 \\cdot %s \\cdot %s}{2} \\approx %s.$$
                Thể tích khối lăng trụ đã cho là:
                $$V = S_{ABCD} \\cdot AA' = %s \\cdot %s = %s.$$'''
                % (val_ad_cd, val_ad_cd, val_dt_day, val_dt_day, val_q_str, val_the_tich))

                # Sửa kqz thành giá trị đúng để dùng cho shortans nếu cần
                dapan = '\\shortans[0]{$%s$}\n' % (val_the_tich)
                # Sắp xếp đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Không dùng tiền tố r ở content theo yêu cầu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

