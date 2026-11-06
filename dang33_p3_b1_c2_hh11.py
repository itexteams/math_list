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


def bt_dang33_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Danh sách các biến thể (đổi tên cạnh hoặc tỉ lệ)
            list_bien_the = ['1']
            bien_the = random.choice(list_bien_the)

            if bien_the == '1':
                # Giả sử cạnh đáy AB = a, Chiều cao AA' = a*sqrt(k)
                # Với k=2, góc giữa AB' và BC' là 60 độ.
                k = 2
                h_coeff = sqrt(k)

                # Đáp án đúng luôn là 60 độ với tỉ lệ này
                da_dung = r'60^\circ'

                # Các phương án nhiễu
                s = [r'30^\circ', r'45^\circ', r'90^\circ', r'120^\circ', r'150^\circ']
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                # Sử dụng latex() để hiển thị công thức đẹp
                noidungcauhoi = ('''Cho hình lăng trụ tam giác đều $ABC.A'B'C'$ có $AB = a$ và $AA' = a\\sqrt{%s}$. Góc giữa hai đường thẳng $AB'$ và $BC'$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 % (latex(k)))

                # --- Bước 2: Tạo hình vẽ bằng TikZ ---
                # Vẽ lăng trụ đứng với các điểm M, N, P, E như trong đề bài
                tikz_code = r'''\begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1] 
            	\draw [line width=1]    (84,28) -- (211.47,29.4) ;
            	\draw [line width=1]    (84,28) -- (130.47,68.07) ;
            	\draw [line width=1]    (130.47,68.07) -- (211.47,29.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (85,151) -- (212.47,152.4) ;
            	\draw [line width=1]    (85,151) -- (131.47,191.07) ;
            	\draw [line width=1]    (131.47,191.07) -- (212.47,152.4) ;
            	\draw [line width=1]    (84,28) -- (85,151) ;
            	\draw [line width=1]    (130.47,68.07) -- (131.47,191.07) ;
            	\draw [line width=1]    (211.47,29.4) -- (212.47,152.4) ;
            	\draw [line width=1]    (130.47,68.07) -- (85,151) ;
            	\draw [line width=1]    (211.47,29.4) -- (131.47,191.07) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (170.97,48.73) -- (108.23,171.03) ;
            	\draw [line width=1]    (170.97,48.73) -- (171.97,171.73) ;
            	\draw [line width=1]    (170.97,48.73) -- (130.47,118.07) ;
            	\draw [line width=1]    (130.47,118.07) -- (108.23,171.03) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (108.23,171.03) -- (171.97,171.73) ;
            	\draw (65,140) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (122,192) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (214,144) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (62,11) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            	\draw (123,40) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            	\draw (214,14) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            	\draw (86,172) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\draw (111,101) node [anchor=north west][inner sep=0.75pt]    {$N$};
            	\draw (159,29) node [anchor=north west][inner sep=0.75pt]    {$P$};
            	\draw (171.97,171.73) node [anchor=north west][inner sep=0.75pt]    {$E$};
            \end{tikzpicture}
            \end{center}'''

                # --- Bước 3: Nội dung lời giải chi tiết ---
                # Tính toán các cạnh (với a=1 để minh họa tỉ lệ)
                # MN = 1/2 AB' = 1/2 * sqrt(a^2 + 2a^2) = a*sqrt(3)/2
                # NP = 1/2 BC' = 1/2 * sqrt(a^2 + 2a^2) = a*sqrt(3)/2
                # MP^2 = ME^2 + EP^2 = (a/2)^2 + (a*sqrt(2))^2 = a^2/4 + 2a^2 = 9a^2/4

                loigiai = (r'''Gọi $M, N, P, E$ lần lượt là trung điểm các đoạn thẳng $AB, BB', B'C', BC$. \\
            Suy ra $MN \parallel AB'$ và $NP \parallel BC'$. Khi đó góc giữa đường thẳng $AB'$ và $BC'$ là góc giữa hai đường thẳng $MN$ và $NP$. \\
            Ta có: $MN = \frac{1}{2}AB' = \frac{1}{2}\sqrt{a^2 + (a\sqrt{2})^2} = \frac{a\sqrt{3}}{2}$. \\
            Tương tự: $NP = \frac{1}{2}BC' = \frac{a\sqrt{3}}{2}$. \\
            Xét tam giác $PEM$ vuông tại $E$, ta có $ME$ là đường trung bình tam giác $ABC \Rightarrow ME = \frac{a}{2}$. \\
            Cạnh $PE = BB' = a\sqrt{2}$. \\
            Do đó $MP^2 = PE^2 + ME^2 = 2a^2 + \frac{a^2}{4} = \frac{9a^2}{4}$. \\
            Áp dụng định lí cosin trong tam giác $MNP$, ta có: \\
            $\cos \widehat{MNP} = \frac{MN^2 + NP^2 - MP^2}{2 \cdot MN \cdot NP} = \frac{\frac{3a^2}{4} + \frac{3a^2}{4} - \frac{9a^2}{4}}{2 \cdot \frac{3a^2}{4}} = \frac{-\frac{3a^2}{4}}{\frac{3a^2}{2}} = -\frac{1}{2}$. \\
            Do đó góc $\widehat{MNP} = 120^\circ$ nên góc giữa hai đường thẳng $AB'$ và $BC'$ bằng $180^\circ - 120^\circ = 60^\circ$.''')
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(60))
                # --- Bước 4: Xuất bản nội dung ---
                da_d = r'\True $' + da_dung + '$'
                list_ans = [da_d, '$' + das1 + '$', '$' + das2 + '$', '$' + das3 + '$']
                random.shuffle(list_ans)


                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n'  + str(noidungcauhoi) + str(dapan)+
                           '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

