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


def bt_dang6_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Ta sẽ random 3 trường hợp góc đẹp: 30, 45, 60 độ
            list_ti_le = [
                {'a': sqrt(3), 'h': 1, 'angle': 30},
                {'a': 1, 'h': 1, 'angle': 45},
                {'a': 1, 'h': sqrt(3), 'angle': 60}
            ]

            case = random.choice(list_ti_le)
            a_val = case['a'] # Độ dài cạnh đáy AB = AC
            h_val = case['h'] # Độ dài cạnh bên AA' = CC'
            kq_dung = case['angle']

            # Tạo các phương án sai (Bước 4)
            s = [30, 45, 60, 75, 90]
            if kq_dung in s:
                s.remove(kq_dung)
            random.shuffle(s)

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Hình vẽ TikZ
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round, scale=1]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.2,-1.2);
                \\coordinate (C) at (3.5,0);
                \\coordinate (A1) at (0,3.5);
                \\coordinate (B1) at (1.2,2.3);
                \\coordinate (C1) at (3.5,3.5);
                \\draw [line width=1pt] (A1)--(B1)--(C1)--cycle;
                \\draw [line width=1pt] (A)--(B)--(C);
                \\draw [line width=1pt, dashed] (A)--(C);
                \\draw [line width=1pt] (A)--(A1) (B)--(B1) (C)--(C1);
                \\draw [line width=1pt,  dashed] (A)--(C1);
                \\draw (A) node[left]{$A$} (B) node[below]{$B$} (C) node[right]{$C$};
                \\draw (A1) node[left]{$A'$} (B1) node[below]{$B'$} (C1) node[right]{$C'$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình lăng trụ đều $ABC.A'B'C'$ có $AB = %s$ và $AA' = %s$. Góc tạo bởi giữa đường thẳng $AC'$ và $(ABC)$ bằng bao nhiêu?'''
                            % (latex(a_val), latex(h_val)))

            # Các đáp án
            da_d = ('\\True $%s^\\circ$' % (kq_dung))
            da_s1 = ('$%s^\\circ$' % (das1))
            da_s2 = ('$%s^\\circ$' % (das2))
            da_s3 = ('$%s^\\circ$' % (das3))

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Lời giải chi tiết
            loigiai = ('''Vì $ABC.A'B'C'$ là hình lăng trụ đều nên $CC' \\perp (ABC)$ và đáy $ABC$ là tam giác đều.\\\\
                        Hình chiếu vuông góc của $AC'$ trên mặt phẳng $(ABC)$ là $AC$.\\\\
                        Do đó, góc giữa đường thẳng $AC'$ và mặt phẳng $(ABC)$ là góc giữa $AC'$ và $AC$, chính là góc $\\widehat{C'AC}$.\\\\
                        Trong tam giác vuông $ACC'$ (vuông tại $C$), ta có:\\\\
                        $\\tan \\widehat{C'AC} = \\frac{CC'}{AC} = \\frac{%s}{%s} = %s$.\\\\
                        Suy ra $\\widehat{C'AC} = %s^\\circ$.''' 
                        % (latex(h_val), latex(a_val), latex(h_val/a_val), kq_dung))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + hinh_ve + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


