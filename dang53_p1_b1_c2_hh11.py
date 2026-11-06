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


def bt_dang53_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số k để AB = CD = 2*k*a
                # MN sẽ được tính toán để ra các góc đẹp: 60, 90
                k = random.randint(1, 3)
                val_ab = 2 * k

                # Danh sách các kịch bản cho MN để tạo góc đẹp
                # (Biểu thức MN, Giá trị MN bình phương/a^2, giá trị cos, góc MPN, góc kết quả)
                scenarios = [
                    (str(k) + 'a\\sqrt{3}', 3*k**2, '-1/2', 120, 60),
                    (str(k) + 'a\\sqrt{2}', 2*k**2, '0', 90, 90),
                    (str(k) + 'a' if k > 1 else 'a', k**2, '1/2', 60, 60)
                ]

                mn_text, mn_sq_coeff, cos_val, angle_mpn, final_angle = random.choice(scenarios)

                # Thiết lập đáp án
                da = '$%s^\\circ$' % final_angle
                options = ['$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$90^\\circ$', '$120^\\circ$']
                if da in options:
                    options.remove(da)

                random.shuffle(options)
                das1, das2, das3 = options[:3]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$ có $AB = CD = %sa$. Gọi $M, N$ lần lượt là trung điểm của $BC$ và $AD$. Biết $MN = %s$. Tính góc giữa $AB$ và $CD$.''' % (latex(val_ab), mn_text))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                mp_val = k
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
                    \\coordinate (B) at (0,0);
                    \\coordinate (C) at (4,0);
                    \\coordinate (D) at (1.5,-1.2);
                    \\coordinate (A) at (1.5,3);
                    \\coordinate (M) at ($(B)!0.5!(C)$);
                    \\coordinate (N) at ($(A)!0.5!(D)$);
                    \\coordinate (P) at ($(A)!0.5!(C)$);
                    \\draw[dashed] (B)--(C) (M)--(N) (M)--(P);
                    \\draw (A)--(B)--(D)--(C)--(A)--(D) (N)--(P);
                    \\filldraw[black] (A)  node[above] {$A$};
                    \\filldraw[black] (B)  node[left] {$B$};
                    \\filldraw[black] (C)  node[right] {$C$};
                    \\filldraw[black] (D)  node[below] {$D$};
                    \\filldraw[black] (M)  node[below] {$M$};
                    \\filldraw[black] (N)  node[right] {$N$};
                    \\filldraw[black] (P)  node[left] {$P$};
                \\end{tikzpicture}
                \\end{center} Gọi $P$ là trung điểm của $AC$. \\\\
                            Trong tam giác $ABC$, $MP$ là đường trung bình nên $MP \\parallel AB$ và $MP = \\frac{AB}{2} = %sa$. \\\\
                            Trong tam giác $ACD$, $NP$ là đường trung bình nên $NP \\parallel CD$ và $NP = \\frac{CD}{2} = %sa$. \\\\
                            Vì $MP \\parallel AB$ và $NP \\parallel CD$ nên góc giữa $AB$ và $CD$ bằng góc giữa $MP$ và $NP$. \\\\
                            Xét tam giác $MNP$, ta có: \\\\
                            $\\cos \\widehat{MPN} = \\frac{MP^2 + NP^2 - MN^2}{2 \\cdot MP \\cdot NP} = \\frac{(%sa)^2 + (%sa)^2 - (%s)^2}{2 \\cdot %sa \\cdot %sa} = %s$. \\\\
                            Suy ra $\\widehat{MPN} = %s^\\circ$. \\\\
                            Vì góc giữa hai đường thẳng luôn nằm trong khoảng $[0^\\circ; 90^\\circ]$ nên góc giữa $AB$ và $CD$ bằng $%s^\\circ$.'''
                           % (latex(mp_val), latex(mp_val), 
                              latex(mp_val), latex(mp_val), mn_text, latex(mp_val), latex(mp_val),
                              cos_val, angle_mpn, final_angle))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

