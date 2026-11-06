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


def bt_dang13_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật và $SA$ vuông góc với mặt phẳng đáy. Gọi $H, K$ theo thứ tự là hình chiếu của $A$ trên các cạnh $SB, SD$.''')

            # Vẽ hình TikZ
            hinh_ve = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (92.47,182.4) -- (254.47,182.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (154.47,129.4) -- (316.47,129.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,182.4) -- (154.47,129.4) ;
            		\draw [line width=1]    (254.47,182.4) -- (316.47,129.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (154.47,129.4) -- (153.47,24.4) ;
            		\draw [line width=1]    (153.47,24.4) -- (316.47,129.4) ;
            		\draw [line width=1]    (153.47,24.4) -- (254.47,182.4) ;
            		\draw [line width=1]    (153.47,24.4) -- (92.47,182.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (154.47,129.4) -- (126.47,97.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (154.47,129.4) -- (209.47,60.4) ;
            		\draw (146,0) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (148,131) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (73,176) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (254.47,182.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (318,118) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (106,79) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (211,39) node [anchor=north west][inner sep=0.75pt]    {$K$};
            	\end{tikzpicture}
            \end{center}''')

            ########################################################################
            # Nhận biết - Mệnh đề a
            nb_da_1_d = '\\True Tam giác $SBC$ vuông'
            nb_da_1_s = 'Tam giác $SBC$ cân tại $S$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $BC \\perp AB$ (do $ABCD$ là hình chữ nhật) và $BC \\perp SA$ (do $SA \\perp (ABCD)$). \\\\
            Suy ra $BC \\perp (SAB) \\Rightarrow BC \\perp SB$. Vậy tam giác $SBC$ vuông tại $B$.''')

            ########################################################################
            # Thông hiểu - Mệnh đề b
            th_da_1_d = '\\True Tam giác $SCD$ vuông'
            th_da_1_s = 'Tam giác $SCD$ đều'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $CD \\perp AD$ (do $ABCD$ là hình chữ nhật) và $CD \\perp SA$ (do $SA \\perp (ABCD)$). \\\\
            Suy ra $CD \\perp (SAD) \\Rightarrow CD \\perp SD$. Vậy tam giác $SCD$ vuông tại $D$.''')

            ########################################################################
            # Vận dụng - Mệnh đề c
            vd_da_1_d = '\\True $SC \\perp (AHK)$'
            vd_da_1_s = '$SC // (AHK)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Ta có $BC \\perp (SAB) \\Rightarrow BC \\perp AH$. Mà $AH \\perp SB$ nên $AH \\perp (SBC) \\Rightarrow AH \\perp SC$. \\\\
            Tương tự, $CD \\perp (SAD) \\Rightarrow CD \\perp AK$. Mà $AK \\perp SD$ nên $AK \\perp (SCD) \\Rightarrow AK \\perp SC$. \\\\
            Vì $SC \\perp AH$ và $SC \\perp AK$ nên $SC \\perp (AHK)$.''')

            ########################################################################
            # Vận dụng cao - Mệnh đề d
            vdc_da_1_d = '\\True $HK \\perp SC$'
            vdc_da_1_s = '$HK$ và $SC$ chéo nhau và không vuông góc'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Theo chứng minh ở câu c, ta có $SC \\perp (AHK)$. \\\\
            Mà đường thẳng $HK$ nằm trong mặt phẳng $(AHK)$. \\\\
            Do đó $SC \\perp HK$ hay $HK \\perp SC$.''')

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng để tạo tính ngẫu nhiên
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' 
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                +hinh_ve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

