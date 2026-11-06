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


def bt_dang7_p3_b4_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Từ điển chứa các hàm lượng giác, giá trị đúng (làm tròn đến hàng phần trăm)
                ans_dict = {
                    '\\sin': {'latex': '\\sin', 'val': '0,87'},
                    '\\cos': {'latex': '\\cos', 'val': '0,50'},
                    '\\tan': {'latex': '\\tan', 'val': '1,73'},
                    '\\cot': {'latex': '\\cot', 'val': '0,58'}
                }

                # Random yêu cầu tính lượng giác của góc
                options = ['\\sin', '\\cos', '\\tan', '\\cot']
                yc = random.choice(options)

                # Kết quả đúng
                kq = ans_dict[yc]['val']

                # Tập hợp các phương án để tạo đáp án nhiễu
                all_vals = ['0,87', '0,50', '1,73', '0,58']
                s = all_vals.copy()
                s.remove(kq)
                random.shuffle(s)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                das1 = '$%s$' % s[0]
                das2 = '$%s$' % s[1]
                das3 = '$%s$' % s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$. Gọi $\\varphi$ là góc giữa hai mặt phẳng $(AB'C')$ và $(AC'D')$. Giá trị $%s \\varphi$ và làm tròn đến hàng phần trăm bằng bao nhiêu?''' % (ans_dict[yc]['latex']))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải có bao gồm vẽ hình TikZ đúng tỉ lệ và góc nhìn
            loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[line width=1pt, scale=1]
                \\coordinate (A1) at (0,0);
                \\coordinate (B1) at (-2,-1.5);
                \\coordinate (D1) at (3,0);
                \\coordinate (C1) at (1,-1.5);
                \\coordinate (A) at (0,3);
                \\coordinate (B) at (-2,1.5);
                \\coordinate (D) at (3,3);
                \\coordinate (C) at (1,1.5);
                \\draw[dashed] (A1) -- (B1);
                \\draw[dashed] (A1) -- (D1);
                \\draw[dashed] (A1) -- (A);
                \\draw (B1) -- (C1) -- (D1);
                \\draw (A) -- (B) -- (C) -- (D) -- cycle;
                \\draw (B) -- (B1);
                \\draw (C) -- (C1);
                \\draw (D) -- (D1);
                \\draw[dashed] (A) -- (C);
                \\draw[dashed] (B1) -- (D1);
                \\draw[dashed] (A) -- (B1);
                \\draw[dashed] (A) -- (C1);
                \\draw[dashed] (A) -- (D1);
                \\draw[dashed] (C) -- (B1);
                \\draw[dashed] (C) -- (D1);
                \\node[above] at (A) {$A$};
                \\node[left] at (B) {$B$};
                \\node[right] at (C) {$C$};
                \\node[right] at (D) {$D$};
                \\node[above right] at (A1) {$A'$};
                \\node[left] at (B1) {$B'$};
                \\node[right] at (C1) {$C'$};
                \\node[right] at (D1) {$D'$};
                \\foreach \\p in {A,B,C,D,A1,B1,C1,D1} \\fill (\\p) circle (1.5pt);
                \\end{tikzpicture}
                \\end{center}
                \\textbf{Nhận xét:} $(AB'C') \\equiv (ADC'B'), (AC'D') \\equiv (ABC'D')$ \\\\
                Ta có: $\\begin{cases} CD' \\perp C'D \\\\ CD' \\perp AD \\text{ (do } AD \\perp (CDD'C')) \\end{cases} \\Rightarrow CD' \\perp (ADC'B') \\quad (1)$ \\\\
                Tương tự: $\\begin{cases} B'C \\perp BC' \\\\ B'C \\perp AB \\text{ (do } AB \\perp (BCC'B')) \\end{cases} \\Rightarrow B'C \\perp (ABC'D') \\quad (2)$ \\\\
                Từ (1) và (2) suy ra $((AB'C'), (AC'D')) = (CD', CB')$. \\\\
                Giả sử cạnh hình lập phương bằng $a$. Ta có $CB' = CD' = B'D' = a\\sqrt{2}$ (đường chéo trong hình vuông) suy ra tam giác $CB'D'$ đều. \\\\
                Do vậy $\\varphi = ((AB'C'), (AC'D')) = (CD', CB') = \\widehat{B'CD'} = 60^\\circ \\Rightarrow %s \\varphi \\approx %s$.''' % (ans_dict[yc]['latex'], kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

