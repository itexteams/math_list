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


def bt_dang51_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['dang1', 'dang2']
            dang = random.choice(lisdang)

            # Khởi tạo các ký hiệu toán học
            a = symbols('a')

            if dang == 'dang1':
                # Trường hợp PQ = a*sqrt(3)/2 -> Góc 60 độ
                val_pq_tex = "\\frac{a\\sqrt{3}}{2}"
                pq_sq = Rational(3, 4) # PQ^2 / a^2
                ans_val = 60
                angle_piq = 120
                cos_val = "- \\frac{1}{2}"

                da_d = "\\True $60^\\circ$"
                s = ["$30^\\circ$", "$45^\\circ$", "$90^\\circ$"]

            elif dang == 'dang2':
                # Trường hợp PQ = a*sqrt(2)/2 -> Góc 90 độ
                val_pq_tex = "\\frac{a\\sqrt{2}}{2}"
                pq_sq = Rational(2, 4) # PQ^2 / a^2
                ans_val = 90
                angle_piq = 90
                cos_val = "0"

                da_d = "\\True $90^\\circ$"
                s = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$"]

            # Trộn đáp án sai
            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            # Tạo danh sách đáp án để xáo trộn trong \choice
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = """\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (1,3.5);
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (1.8,-1);
                \\coordinate (D) at (4.5,0.2);
                \\coordinate (P) at (0.9,-0.5); 
                \\coordinate (Q) at (2.75,1.85); 
                \\coordinate (I) at (1.4,1.25); 
                \\draw (A)--(B)--(C)--(D)--(A)--(C) (I)--(P) (I)--(Q);
                \\draw[dashed] (B)--(D) (P)--(Q)  ;
                \\fill (A)  node[above] {$A$};
                \\fill (B)  node[left] {$B$};
                \\fill (C)  node[below] {$C$};
                \\fill (D)  node[right] {$D$};
                \\fill (P)  node[left] {$P$};
                \\fill (Q)  node[right] {$Q$};
                \\fill (I)  node[left] {$I$};
            \\end{tikzpicture}
            \\end{center}"""

            # Câu hỏi
            noidungcauhoi = ("Cho tứ diện $ABCD$. Gọi $P, Q$ lần lượt là trung điểm của các cạnh $BC, AD$. Giả sử "
                             "$AB = CD = a$ và $PQ = %s$. Số đo góc giữa hai đường thẳng $AB$ và $CD$ là" 
                             % (val_pq_tex))

            # Lời giải chi tiết
            loigiai = ("Gọi $I$ là trung điểm của $AC$. \\\\ "
                       "Khi đó $IP$ là đường trung bình của tam giác $ABC \\implies IP \\parallel AB$ và $IP = \\frac{AB}{2} = \\frac{a}{2}$. \\\\ "
                       "Tương tự, $IQ$ là đường trung bình của tam giác $ACD \\implies IQ \\parallel CD$ và $IQ = \\frac{CD}{2} = \\frac{a}{2}$. \\\\ "
                       "Suy ra góc giữa hai đường thẳng $AB$ và $CD$ là góc giữa hai đường thẳng $IP$ và $IQ$. \\\\ "
                       "Xét tam giác $IPQ$, ta có: \\\\ "
                       "$\\cos \\widehat{PIQ} = \\frac{IP^2 + IQ^2 - PQ^2}{2 \\cdot IP \\cdot IQ} = \\frac{\\left(\\frac{a}{2}\\right)^2 + \\left(\\frac{a}{2}\\right)^2 - \\left(%s\\right)^2}{2 \\cdot \\frac{a}{2} \\cdot \\frac{a}{2}} = %s$. \\\\ "
                       "Suy ra $\\widehat{PIQ} = %s^\\circ$. \\\\ "
                       "Vì góc giữa hai đường thẳng luôn $\\le 90^\\circ$ nên số đo góc giữa $AB$ và $CD$ là $%s^\\circ$." 
                       % (val_pq_tex, cos_val, angle_piq, ans_val))

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(tikz_code) + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

