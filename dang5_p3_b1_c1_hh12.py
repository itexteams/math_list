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


def bt_dang5_p3_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(10,50)
                d1=a*sqrt(3)
                number = Decimal(float(d1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một chiếc đèn được treo song song với mặt phẳng nằm ngang bởi ba sợi dây không giãn xuất phát từ điểm $O$ '
                                'trên trần nhà và lần lượt buộc vào ba điểm $A,B,C$ trên đèn tròn sao cho các lực căng $\\vec{F_1},\\vec{F_2},\\vec{F_3}$ lần lượt trên dây nối $OA,OB,OC$ đôi một vuông góc với nhau '
                                'và $\\abs{\\vec{F_1}}=\\abs{\\vec{F_2}}=\\abs{\\vec{F_3}}=%s$(N) (như hình vẽ)$zz$ Hỏi trọng lượng của chiếc đèn tròn đó bằng bao nhiêu Newton? (làm tròn kết quả đến hàng đơn vị)$zz$'
                                '}{'
                                '''
                                \\definecolor{ffqqqq}{rgb}{1$zz$,0$zz$,0$zz$}
                                '\\scalebox{0$zz$6}{ '
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-3$zz$5018443859090067,-3$zz$2594319584779825) rectangle (3$zz$5903951362890627,5$zz$807509548332079);
                \\fill[line width=1$zz$pt,fill=black,pattern=north east lines,pattern color=black] (-2$zz$,5$zz$) -- (2$zz$,5$zz$) -- (2$zz$0139205045277446,5$zz$408017981662814) -- (-2$zz$006279438536401,5$zz$408017981662814) -- cycle;
                \\draw [rotate around={0$zz$:(0$zz$,0$zz$)},line width=1$zz$pt] (0$zz$,0$zz$) ellipse (2$zz$2882456112707374cm and 1$zz$111785940502843cm);
                \\draw [line width=1$zz$pt] (-2$zz$2882456112707374,0$zz$)-- (-2$zz$275131461388665,-0$zz$5664988543722905);
                \\draw [line width=1$zz$pt] (2$zz$2882456112707374,0$zz$)-- (2$zz$2813454189935207,-0$zz$6201044647297278);
                \\draw [shift={(0$zz$03194986111782334,1$zz$8583433372576157)},line width=1$zz$pt]  plot[domain=3$zz$9518721504673895:5$zz$449377484002473,variable=\\t]({1$zz$*3$zz$3470111865613497*cos(\\t r)+0$zz$*3$zz$3470111865613497*sin(\\t r)},{0$zz$*3$zz$3470111865613497*cos(\\t r)+1$zz$*3$zz$3470111865613497*sin(\\t r)});
                \\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (0$zz$,0$zz$)-- (2$zz$2882456112707374,0$zz$);
                \\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (0$zz$,0$zz$)-- (0$zz$,-1$zz$4885153525202133);
                \\draw [line width=1$zz$pt] (0$zz$,5$zz$)-- (2$zz$2882456112707374,0$zz$);
                \\draw [line width=1$zz$pt] (0$zz$,5$zz$)-- (-2$zz$1157654381919273,-0$zz$42345993765770873);
                \\draw [line width=1$zz$pt] (0$zz$,5$zz$)-- (-1$zz$,1$zz$);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,-1$zz$4885153525202133) -- (0$zz$,-3$zz$);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,5$zz$) -- (1$zz$2585378940871805,2$zz$249993864539145);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,5$zz$) -- (-0$zz$6132180805615,2$zz$5471276777540033);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,5$zz$) -- (-1$zz$2428238823280127,1$zz$81419999887589);
                \\draw [line width=1$zz$pt] (-2$zz$,5$zz$)-- (2$zz$,5$zz$);
                \\draw [line width=1$zz$pt] (2$zz$,5$zz$)-- (2$zz$0139205045277446,5$zz$408017981662814);
                \\draw [line width=1$zz$pt] (2$zz$0139205045277446,5$zz$408017981662814)-- (-2$zz$006279438536401,5$zz$408017981662814);
                \\draw [line width=1$zz$pt] (-2$zz$006279438536401,5$zz$408017981662814)-- (-2$zz$,5$zz$);
                \\draw (-0$zz$8040120970728782,5) node[anchor=north west] {$O$};
                \\draw (-1$zz$9582393134306033,2$zz$720299403375279) node[anchor=north west] {$\\vec{F}_1$};
                \\draw (-0$zz$5397914089909894,3$zz$2765534835476755) node[anchor=north west] {$\\vec{F}_2$};
                \\draw (1$zz$2402216475606829,3$zz$1653026675131963) node[anchor=north west] {$\\vec{F}_3$};
                \\draw (-2$zz$1390218894866324,0$zz$20324969059518536) node[anchor=north west] {$A$};
                \\draw (-1$zz$1377645451763168,1$zz$204507034905499) node[anchor=north west] {$B$};
                \\draw (2$zz$3110107518925482,0$zz$5091894346900033) node[anchor=north west] {$C$};
                \\draw (0$zz$016462671181408168,-2$zz$2581746141676686) node[anchor=north west] {$\\vec{P}$};
            \\end{tikzpicture}}
                                '''
                                '}'

                                %(latex(a))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $A_1,B_1,C_1$ lần lượt là các điểm sao cho $\\abs{\\vec{OA_1}}=\\abs{\\vec{F_1}},\\abs{\\vec{OB_1}}=\\abs{\\vec{F_2}},\\abs{\\vec{OC_1}}=\\abs{\\vec{F_3}}$$zz$ Lấy các điểm $D_1,A_1\',B_1\',D_1\'$ '
                        'sao cho $OA_1D_1B_1$zz$C_1A_1\',D_1\',B_1\'$ là hình hộp như hình dưới đây$zz$\\\\ \n'
                        'Theo quy tắc hình bình hộp ta có $\\vec{OA_1}+\\vec{OB_1}+\\vec{OC_1}=\\vec{OD_1\'}$$zz$\\\\ \n'
                        'Mặt khác, do các lực căng $\\vec{F_1},\\vec{F_2},\\vec{F_3}$ đôi một vuông góc và $\\abs{\\vec{F_1}}=\\abs{\\vec{F_2}}=\\abs{\\vec{F_3}}=%s$(N) nên hình hộp $OA_1D_1B_1$zz$C_1A_1\',D_1\',B_1\'$ có ba cạnh $OA_1,OB_1,OC_1$ đôi một vuông góc và bằng nhau$zz$ '
                        'Do đó hình hộp $OA_1D_1B_1$zz$C_1A_1\',D_1\',B_1\'$ là hình lập phương có độ dài cạnh bằng $%s$$zz$\\\\ \n'
                        'Suy ra độ dài đường chéo của hình lập phương đó bằng $%s\\sqrt{3}$$zz$\\\\ \n'
                        'Do chiếc đèn ở vị trí cân bằng nên $\\vec{F_1}+\\vec{F_2}+\\vec{F_3}=\\vec{P}$, trong đó $\\vec{P}$ là trọng lực tác dụng lên chiếc đèn$zz$\\\\ \n'
                        'Vậy trọng lượng của chiến đèn là $\\abs{\\vec{P}}=\\abs{\\vec{OD_1\'}}=%s\\sqrt{3} \\approx %s$(N)$zz$'

                        %(latex(a),latex(a),latex(a),latex(a),latex(kq))  
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

