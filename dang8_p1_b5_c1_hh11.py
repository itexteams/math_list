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


def bt_dang8_p1_b5_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Vẽ hình TikZ 100% theo mẫu: nét 1pt, điểm 1pt, màu black, không random tọa độ
        hinh_ve = '''\\begin{center}
        	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
        		\\draw [line width=1]    (189.1,144.9) -- (323.6,144.9) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (289.1,92.4) -- (305.6,144.4) ;
        		\\draw [line width=1]    (229.6,74.4) -- (253.1,144.9) ;
        		\\draw [line width=1]    (187.6,88.9) -- (293.6,52.4) ;
        		\\draw [line width=1]    (230.6,172.9) -- (365.1,172.9) ;
        		\\draw [line width=1]    (321.6,87.9) -- (350.1,172.4) ;
        		\\draw [line width=1]    (274.6,101.9) -- (297.85,172.9) ;
        		\\draw [line width=1]    (274.6,101.9) -- (321.6,87.9) ;
        		\\draw [line width=1]    (251.6,66.9) -- (277.1,145.4) ;
        		\\draw [line width=1]    (207.6,81.9) -- (227.6,145.4) ;
        		\\draw [line width=1]    (111.1,52.9) -- (134.35,123.9) ;
        		\\draw [line width=1]    (289.1,92.4) -- (276.6,57.9) ;
        		\\draw [line width=1]    (394.1,196.4) -- (105.6,196.4) ;
        		\\draw [line width=1]    (173.1,129.9) -- (105.6,196.4) ;
        		\\draw (118,179) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$P)$};
        		\\draw (262,83.5) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A$};
        		\\draw (314.5,70) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B$};
        		\\draw (289,175) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A'$};
        		\\draw (346.5,175) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B'$};
        		\\draw (194,62) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$C$};
        		\\draw (219,54) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$D$};
        		\\draw (240.5,48) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$E$};
        		\\draw (266,39) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$G$};
        		\\draw (108,78) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$d$};
        		\\draw (211,147) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$C'$};
        		\\draw (244.5,147) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$D'$};
        		\\draw (269.5,146) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$E'$};
        		\\draw (297.5,145) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$G'$};
        	\\end{tikzpicture}
        \\end{center}'''

        # Nội dung câu hỏi (sử dụng // thay cho ||)
        cauhoi_text = (
            "Trên hình vẽ, ta có phép chiếu song song theo phương $d$ lên mặt phẳng chiếu $(P)$; "
            "$AB // CG$ và $AB = DG$; $A', B', C', D', E', G'$ lần lượt là hình chiếu của $A, B, C, D, E, G$ qua phép chiếu nói trên.\\\\"
            + hinh_ve + "Mệnh đề nào sau đây đúng?"
        )
        noidungcauhoi = "%s" % (cauhoi_text)

        # Các mệnh đề thành phần
        md_A = "$\\dfrac{DG}{AB} = \\dfrac{D'G'}{A'B'} = 1$"
        md_B = "$\\dfrac{C'D'}{D'E'} = \\dfrac{CD}{DE}$"
        md_C = "$D'G' = A'B'$"

        # Đáp án đúng
        du = [
            "Các mệnh đề %s, %s và %s đều đúng" % (md_A, md_B, md_C)
        ]
        da = random.choice(du)

        # Các đáp án sai
        s = [
            "Chỉ có mệnh đề %s là đúng" % (md_A),
            "Chỉ có mệnh đề %s là đúng" % (md_B),
            "Chỉ có mệnh đề %s là đúng" % (md_C),
            "$\\dfrac{C'D'}{D'E'} = \\dfrac{DE}{CD}$",
            "Tất cả các mệnh đề trên đều sai"
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Gán cờ \True cho đáp án đúng
        da_d = "\\True " + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết, rõ ràng từng bước, chuẩn quy tắc LaTeX
        loigiai_text = (
            "Theo các tính chất của phép chiếu song song lên mặt phẳng $(P)$, ta có:\\\\"
            "+ Phép chiếu song song bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng hoặc nằm trên hai đường thẳng song song.\\\\"
            "1. Vì các điểm $C, D, E$ cùng nằm trên một đường thẳng và có hình chiếu lần lượt là $C', D', E'$ nên:\\\\"
            "$\\dfrac{C'D'}{D'E'} = \\dfrac{CD}{DE}$. Suy ra mệnh đề %s đúng.\\\\"
            "2. Do $AB // CG$ và $D, G$ thuộc đường thẳng $CG$ nên hai đoạn thẳng $AB$ và $DG$ nằm trên hai đường thẳng song song với nhau.\\\\"
            "Do đó, tỉ số độ dài của chúng được bảo toàn qua phép chiếu song song:\\\\"
            "$\\dfrac{D'G'}{A'B'} = \\dfrac{DG}{AB}$.\\\\"
            "Theo giả thiết đề bài $AB = DG$, suy ra $\\dfrac{DG}{AB} = 1$.\\\\"
            "Từ đó ta có: $\\dfrac{DG}{AB} = \\dfrac{D'G'}{A'B'} = 1$. Suy ra mệnh đề %s đúng.\\\\"
            "3. Từ $\\dfrac{D'G'}{A'B'} = 1$, ta suy ra ngay $D'G' = A'B'$. Do đó mệnh đề %s đúng.\\\\"
            "Vậy các mệnh đề %s, %s và %s đều đúng."
            % (md_B, md_A, md_C, md_A, md_B, md_C)
        )
        loigiai = "%s" % (loigiai_text)

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n'
        '\\choice\n'
        '{' + str(list_1[0]) + '}\n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
    return content

