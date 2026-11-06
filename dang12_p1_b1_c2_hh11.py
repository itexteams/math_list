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


def bt_dang12_p1_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            cd=randint(220,240)
            sc=randint(210,230)
            hc=Rational(cd,2)
            goc1=acos(hc/sc)
            goc2=goc1*180/pi

            h1=goc2   
            number = Decimal(float(h1))  # Số cần làm tròn
            goc = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

            if dang=='1':

                du = ['$%s^\\circ$'%(latex(goc)),
                    ]
                da= random.choice(du)
                s = ['$%s^\\circ$'%(latex(goc+1)),
                    '$%s^\\circ$'%(latex(goc+2)),
                    '$%s^\\circ$'%(latex(goc+3)),
                    '$%s^\\circ$'%(latex(goc-1)),
                    '$%s^\\circ$'%(latex(goc-2)),
                    '$%s^\\circ$'%(latex(goc-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Kim tự tháp Cheops là kim tự tháp lớn nhất trong các kim tự tháp ở Ai Cập, được 
            xây dựng vào thế kỉ thứ $26$ trước Công nguyên và là một trong bảy kì quan của thế giới 
            cổ đạizz Kim tự tháp có dạng hình chóp với đáy là hình vuông có cạnh dài khoảng $%s$ m, các 
            cạnh bên bằng nhau và dài khoảng $%s$ m (kích thước hiện nay)zz 
                                \\begin{center}
                \\definecolor{zzttqq}{rgb}{0zz6,0zz2,0zz}
                \\definecolor{ffxfqq}{rgb}{1zz,0zz4980392156862745,0zz}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1zz8372784620064704,-0zz388119664046677) rectangle (7zz340848479425471,3zz3590477510660572);
                    \\fill[line width=1zzpt,color=ffxfqq,fill=ffxfqq,fill opacity=0zz3199999928474426] (2zz8676594179691803,2zz872176244128584) -- (0zz5098438064361294,0zz5574257579203378) -- (3zz589000267159657,0zz4605292259395275) -- cycle;
                    \\fill[line width=1zzpt,color=zzttqq,fill=zzttqq,fill opacity=0zz4300000071525574] (2zz8676594179691803,2zz872176244128584) -- (3zz589000267159657,0zz4605292259395275) -- (5zz440800656126254,0zz5251269139267344) -- cycle;
                    \\fill[line width=1zzpt,color=zzttqq,fill=zzttqq,fill opacity=0zz6600000262260437] (0zz9604800871463178,0zz9998312389828516) -- (0zz,1zz) -- (-1zz5,0zz) -- (7zz,0zz) -- (6zz,1zz) -- (4zz918922140734711,1zz0011499949114888) -- (5zz440800656126254,0zz5251269139267344) -- (3zz589000267159657,0zz4605292259395275) -- (0zz5098438064361294,0zz5574257579203378) -- cycle;
                    \\draw [line width=1zzpt] (0zz5098438064361294,0zz5574257579203378)-- (2zz8676594179691803,2zz872176244128584);
                    \\draw [line width=1zzpt] (2zz8676594179691803,2zz872176244128584)-- (3zz589000267159657,0zz4605292259395275);
                    \\draw [line width=1zzpt] (3zz589000267159657,0zz4605292259395275)-- (0zz5098438064361294,0zz5574257579203378);
                    \\draw [line width=1zzpt] (3zz589000267159657,0zz4605292259395275)-- (5zz440800656126254,0zz5251269139267344);
                    \\draw [line width=1zzpt] (5zz440800656126254,0zz5251269139267344)-- (2zz8676594179691803,2zz872176244128584);
                    \\draw [line width=1zzpt,color=ffxfqq] (2zz8676594179691803,2zz872176244128584)-- (0zz5098438064361294,0zz5574257579203378);
                    \\draw [line width=1zzpt,color=ffxfqq] (0zz5098438064361294,0zz5574257579203378)-- (3zz589000267159657,0zz4605292259395275);
                    \\draw [line width=1zzpt,color=ffxfqq] (3zz589000267159657,0zz4605292259395275)-- (2zz8676594179691803,2zz872176244128584);
                    \\draw [line width=1zzpt,color=zzttqq] (2zz8676594179691803,2zz872176244128584)-- (3zz589000267159657,0zz4605292259395275);
                    \\draw [line width=1zzpt,color=zzttqq] (3zz589000267159657,0zz4605292259395275)-- (5zz440800656126254,0zz5251269139267344);
                    \\draw [line width=1zzpt,color=zzttqq] (5zz440800656126254,0zz5251269139267344)-- (2zz8676594179691803,2zz872176244128584);
                    \\draw [line width=1zzpt] (0zz,1zz)-- (0zz9604800871463178,0zz9998312389828516);
                    \\draw [line width=1zzpt] (4zz918922140734711,1zz0011499949114888)-- (6zz,1zz);
                    \\draw [line width=1zzpt] (0zz,1zz)-- (-1zz5,0zz);
                    \\draw [line width=1zzpt] (-1zz5,0zz)-- (7zz,0zz);
                    \\draw [line width=1zzpt] (7zz,0zz)-- (6zz,1zz);
                    \\draw [line width=1zzpt,color=zzttqq] (0zz9604800871463178,0zz9998312389828516)-- (0zz,1zz);
                    \\draw [line width=1zzpt,color=zzttqq] (0zz,1zz)-- (-1zz5,0zz);
                    \\draw [line width=1zzpt,color=zzttqq] (-1zz5,0zz)-- (7zz,0zz);
                    \\draw [line width=1zzpt,color=zzttqq] (7zz,0zz)-- (6zz,1zz);
                    \\draw [line width=1zzpt,color=zzttqq] (6zz,1zz)-- (4zz918922140734711,1zz0011499949114888);
                    \\draw [line width=1zzpt,color=zzttqq] (4zz918922140734711,1zz0011499949114888)-- (5zz440800656126254,0zz5251269139267344);
                    \\draw [line width=1zzpt,color=zzttqq] (5zz440800656126254,0zz5251269139267344)-- (3zz589000267159657,0zz4605292259395275);
                    \\draw [line width=1zzpt,color=zzttqq] (3zz589000267159657,0zz4605292259395275)-- (0zz5098438064361294,0zz5574257579203378);
                    \\draw [line width=1zzpt,color=zzttqq] (0zz5098438064361294,0zz5574257579203378)-- (0zz9604800871463178,0zz9998312389828516);
                    \\draw [line width=1zzpt] (2zz8676594179691803,2zz872176244128584)-- (0zz5098438064361294,0zz5574257579203378);
                    \\draw [line width=1zzpt] (2zz8676594179691803,2zz872176244128584)-- (3zz589000267159657,0zz4605292259395275);
                    \\draw [line width=1zzpt] (2zz8676594179691803,2zz872176244128584)-- (5zz440800656126254,0zz5251269139267344);
                    \\draw [line width=1zzpt] (0zz5098438064361294,0zz5574257579203378)-- (3zz589000267159657,0zz4605292259395275);
                    \\draw [line width=1zzpt] (3zz589000267159657,0zz4605292259395275)-- (5zz440800656126254,0zz5251269139267344);
                    \\draw (2zz6,3zz397979360573722) node[anchor=north west] {$S$};
                    \\draw (0,0zz7) node[anchor=north west] {$A$};
                    \\draw (3zz2,0zz5) node[anchor=north west] {$B$};
                    \\draw (5zz3,0zz7) node[anchor=north west] {$C$};
                \\end{tikzpicture}
            \\end{center}
            Góc tạo bởi cạnh bên $SC$ và cạnh đáy $AB$ của kim tự tháp là'''
                                %(latex(cd),latex(sc)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-0zz5371640736480506,-0zz4471838892378394) rectangle (6zz508835179123402,4zz15078228981431);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (2zz5,3zz5);
                    \\draw [line width=1zzpt] (2zz5,3zz5)-- (4zz,0zz);
                    \\draw [line width=1zzpt] (4zz,0zz)-- (0zz,0zz);
                    \\draw [line width=1zzpt] (4zz,0zz)-- (6zz,1zz);
                    \\draw [line width=1zzpt] (6zz,1zz)-- (2zz5,3zz5);
                    \\draw [line width=1zzpt] (2zz5,3zz5)-- (0zz,0zz);
                    \\draw [line width=1zzpt] (2zz5,3zz5)-- (4zz,0zz);
                    \\draw [line width=1zzpt] (2zz5,3zz5)-- (6zz,1zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (4zz,0zz);
                    \\draw [line width=1zzpt] (4zz,0zz)-- (6zz,1zz);
                    \\draw (2zz26,4zz2) node[anchor=north west] {$S$};
                    \\draw (-0zz5,0zz16708271228582686) node[anchor=north west] {$A$};
                    \\draw (3zz9,0zz0677160561569985) node[anchor=north west] {$B$};
                    \\draw (6,1zz1607492735741105) node[anchor=north west] {$C$};
                    \\draw [line width=1zzpt,dashed] (6zz,1zz)-- (2zz,1zz);
                    \\draw [line width=1zzpt,dashed] (2zz,1zz)-- (0zz,0zz);
                    \\draw [line width=1zzpt,dashed] (2zz,1zz)-- (2zz5,3zz5);
                    \\draw [line width=1zzpt,dashed] (2zz5,3zz5)-- (4zz001194587923694,1zz);
                    \\draw (1zz3,1zz3685159182071154) node[anchor=north west] {$D$};
                    \\draw (3zz8440021283957373,1zz0704159498206303) node[anchor=north west] {$H$};
                \\end{tikzpicture}
            \\end{center}                           
                        Vì $ABCD$ là hình vuông nên $AB // CD$zz \\\\
                        Khi đó $(SC, AB) = (SC, CD) = \\widehat{SCD}$zz \\\\
                        Gọi $H$ là trung điểm của $CD$, suy ra \\\\
                        $DH = HC = \\dfrac{CD}{2} = \\dfrac{%s}{2} = %s$ mzz \\\\
                        Vì tam giác $SCD$ có $SC = SD$ nên tam giác $SCD$ cân tại $S$ mà $SH$ là trung tuyến nên $SH$ là đường caozz \\\\
                        Xét tam giác $SHC$ vuông tại $H$ ta có \\\\
                        $\\cos{SCD} = \\cos{SCH} = \\dfrac{HC}{SC} = \\dfrac{%s}{%s} \\Rightarrow \\widehat{SCD} \\approx %s^\\circ$zz \\\\
                        Vậy góc tạo bởi cạnh bên $SC$ và cạnh đáy $AB$ của kim tự tháp khoảng $%s^\\circ$zz'''
                        %(latex(cd),latex(hc),latex(hc),latex(sc),latex(goc),latex(goc)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content

